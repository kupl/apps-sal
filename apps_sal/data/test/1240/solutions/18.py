from sys import stdin as fin

n = int(fin.readline())
l, r = [None] * n, [None] * n
ls = rs = 0
for i in range(n):
    l[i], r[i] = map(int, fin.readline().strip().split())
    ls += l[i]
    rs += r[i]

maxv = abs(ls - rs)
maxi = None
for i in range(n):
    nabs = abs((ls - l[i] + r[i]) - (rs - r[i] + l[i]))
    if nabs > maxv:
        maxv = nabs
        maxi = i

print(maxi + 1 if maxi is not None else 0)
