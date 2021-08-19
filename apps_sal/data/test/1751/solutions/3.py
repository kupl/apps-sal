from collections import *
from sys import stdin, stderr


def rl():
    return [int(w) for w in stdin.readline().split()]


MOD = 1000000007
(n,) = rl()
r = 0
i1f = 1
for i in range(2, n + 1):
    r = (2 * r + i1f * (i - 2)) % MOD
    i1f = i1f * i % MOD
print(r)
