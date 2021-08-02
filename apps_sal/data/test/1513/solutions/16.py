import sys
from math import *


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return map(int, minp().split())


n, m, k = mints()
b = list(mints())
c = [0] * (n - 1)
for i in range(1, len(b)):
    c[i - 1] = b[i] - b[i - 1] - 1
c.sort()
r = n
for i in range(n - k):
    r += c[i]
print(r)
