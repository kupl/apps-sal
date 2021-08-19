import sys
from math import *
f = open('input.txt', 'r')
out = open('output.txt', 'w')


def minp():
    return f.readline().strip()


def mint():
    return int(minp())


def mints():
    return map(int, minp().split())


(n, k) = mints()
a = []
j = 0
for i in mints():
    j += 1
    a.append((-i, j))
a.sort()
print(-a[k - 1][0], file=out)
for i in range(k):
    print(a[i][1], end=' ', file=out)
f.close()
out.close()
