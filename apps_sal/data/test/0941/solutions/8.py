import sys
from math import *


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


b, k = mints()
z = 0
for i in mints():
    z = z * b + i
    z = (z & 1)
if z == 0:
    print("even")
else:
    print("odd")
