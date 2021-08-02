from itertools import permutations

n = int(input())

l = [[int(x) for x in input().split()] for _ in range(n)]

s = set()


def add(t, cur, lvl):
    for i in range(6):
        print
        cur2 = cur * 10 + l[t[lvl]][i]
        s.add(cur2)
        if lvl < n - 1:
            add(t, cur2, lvl + 1)


for t in permutations(tuple(range(n))):
    add(t, 0, 0)

a = 1
while True:
    if a in s:
        a += 1
    else:
        print(a - 1)
        break
