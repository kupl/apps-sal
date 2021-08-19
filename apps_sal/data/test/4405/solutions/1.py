import sys
from math import *


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return map(int, minp().split())


n = mints()
a = list(mints())
a.sort()
p = -1
c = -1
b = []
for i in range(len(a)):
    if a[i] != p:
        if c != -1:
            b.append((c, p))
        c = 1
        p = a[i]
    else:
        c += 1
if c != -1:
    b.append((c, p))
b.sort(reverse=True)
p = -1
r = 0
for i in range(len(b)):
    if p == -1:
        p = b[i][0]
    else:
        p = min(p // 2, b[i][0])
    if p != 0:
        r = max(r, p * (2 ** (i + 1) - 1))
print(r)
