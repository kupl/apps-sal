import sys
from math import *


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return map(int, minp().split())


(n, k) = mints()
x = 1
pows = []
if k == 1:
    pows = [1]
elif k == -1:
    pows = [1, -1]
else:
    m = 10 ** (9 + 5)
    while x <= m:
        pows.append(x)
        x *= k
a = list(mints())
s = 0
z = dict()
z[0] = 1
r = 0
for i in range(n):
    s += a[i]
    z[s] = z.get(s, 0) + 1
    for j in pows:
        if s - j in z:
            r += z[s - j]
print(r)
