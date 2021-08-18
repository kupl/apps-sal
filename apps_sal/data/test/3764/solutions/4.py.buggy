#!/usr/bin/env python3
from sys import stdin, stdout


def ri():
    return list(map(int, input().split()))


n, k, x = ri()
a = []
a.append(list(ri()))

t = 0
j = 0
goout = 0
for j in range(0, k):
    a[j].sort()
    if j != 0:
        for t in range(j):
            if a[t] == a[j]:
                goout = 1
                break
    if goout:
        break
    a.append([a[j][i] ^ x if not i % 2 else a[j][i] for i in range(n)])
else:
    a[k].sort()
    print(a[k][-1], a[k][0])
    return

m = t + (k - t) % (j - t)
print(a[m][-1], a[m][0])
