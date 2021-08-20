import sys
from math import *


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


(n, x) = mints()
x -= 1
a = list(mints())
m = min(a)
d = max(0, m - 2)
if d != 0:
    for i in range(n):
        a[i] -= d
t = n * d
while True:
    a[x] -= 1
    t += 1
    x = (x + n - 1) % n
    if a[x] == 0:
        break
a[x] = t
print(*a)
