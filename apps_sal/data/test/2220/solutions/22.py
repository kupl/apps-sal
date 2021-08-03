import sys
from math import *


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return map(int, minp().split())


n, m, k = mints()
a = list(mints())
a.sort()
b = a[-1]
c = a[-2]
z = m // (k + 1)
print((m - z) * b + c * z)
