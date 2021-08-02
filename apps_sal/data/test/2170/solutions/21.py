from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque, Counter
from operator import mul
from functools import reduce


N = 10**6
mod = 10**9 + 7

inv_t = [0] + [1]
for i in range(2, N):
    inv_t += [inv_t[mod % i] * (mod - int(mod / i)) % mod]

kai = [1, 1]
rev_kai = [1, inv_t[1]]
for i in range(2, N):
    kai.append(kai[-1] * i % mod)
    rev_kai.append(rev_kai[-1] * inv_t[i] % mod)


def cmb(n, r):
    return kai[n] * rev_kai[r] * rev_kai[n - r] % mod


def prm(n, r):
    return kai[n] * rev_kai[n - r] % mod


n, m = list(map(int, input().split()))

a = 0
for k in range(n + 1):
    a += prm(m, k) * prm(m - k, n - k)**2 * (-1)**k * cmb(n, k) % mod

print(a % mod)
