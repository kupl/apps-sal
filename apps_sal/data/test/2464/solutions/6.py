import sys


class Disjoint:
    def __init__(self, n):
        self.n = n
        self.size = [1] * self.n
        self.parent = [i for i in range(self.n)]

    def root(self, node):
        self.parent[node] = node if self.parent[node] == node else self.root(self.parent[node])
        return self.parent[node]

    def join(self, a, b):
        a = self.root(a)
        b = self.root(b)
        if a == b:
            return False
        if self.size[a] > self.size[b]:
            a, b = b, a

        self.size[b] += self.size[a]
        self.parent[a] = b
        return True


inp = [int(x) for x in sys.stdin.read().split()]
n = inp[0]

white = Disjoint(n)
black = Disjoint(n)

inp_idx = 1
for i in range(n - 1):
    x, y, c = inp[inp_idx], inp[inp_idx + 1], inp[inp_idx + 2]
    x -= 1
    y -= 1
    inp_idx += 3

    if c == 0:
        white.join(x, y)
    else:
        black.join(x, y)

ans = 0
for i in range(n):
    rootW = white.root(i)
    rootB = black.root(i)
    ans += white.size[rootW] - 1
    ans += black.size[rootB] - 1

    ans += (white.size[rootW] - 1) * (black.size[rootB] - 1)

print(ans)
