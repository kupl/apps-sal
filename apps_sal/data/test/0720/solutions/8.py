from math import *
import sys


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return map(int, minp().split())


n = mint()
(pa, pb) = (0, 0)
pl = 0
c = 0
for i in range(n):
    (a, b) = mints()
    l = max(max(pa, pb), pl)
    r = min(a, b)
    if r >= l:
        c += r - l + 1
        pl = r + 1
    (pa, pb) = (a, b)
print(c)
