

from collections import deque


n = int(input())
ligths = [0, 0] + [int(x) for x in input().split()]

prefix_tree = [0 for _ in range(len(ligths))]

q = deque()
q.append(1)
while len(q):
    m = q.pop()
    prefix_tree[m] = ligths[m] + prefix_tree[m // 2]

    if m * 2 + 1 < len(ligths):
        q.append(m * 2)
        q.append(m * 2 + 1)

needed_lights = max(prefix_tree)


suffix_tree = [0 for _ in range(len(ligths))]


def pocitaj(i):
    if i >= len(ligths):
        return

    pocitaj(i * 2)
    pocitaj(i * 2 + 1)

    if i >= len(ligths) // 2:
        suffix_tree[i] = ligths[i]
    else:
        suffix_tree[i] = max(suffix_tree[i * 2], suffix_tree[i * 2 + 1]) + ligths[i]


pocitaj(1)
suffix_tree += [needed_lights for _ in range(len(ligths))]


class Test:
    def __init__(self):
        self.ans = 0
        self.vypocitaj(1)

    def vypocitaj(self, i):

        if suffix_tree[i * 2] < suffix_tree[i * 2 + 1]:
            rozdiel = suffix_tree[i * 2 + 1] - suffix_tree[i * 2]
            self.ans += rozdiel
        else:
            rozdiel = suffix_tree[i * 2] - suffix_tree[i * 2 + 1]
            self.ans += rozdiel

        if i * 2 + 1 < len(ligths):
            self.vypocitaj(i * 2)
            self.vypocitaj(i * 2 + 1)


ans = Test()
print(ans.ans)
