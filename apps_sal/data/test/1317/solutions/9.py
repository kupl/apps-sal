import sys
from math import *


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return map(int, minp().split())


(n, m) = mints()
k = n // m
c = [0] * m
for i in range(m):
    c[i * i % m] += k
c[0] -= 1
for i in range(k * m, n + 1):
    c[i * i % m] += 1
r = 0
c.append(c[0])
for i in range(m):
    r += c[i] * c[m - i]
print(r)
