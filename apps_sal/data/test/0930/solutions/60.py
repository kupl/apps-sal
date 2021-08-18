from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque, Counter
from operator import mul
import copy
import heapq

n, k = list(map(int, input().split()))

m = 4 * 10**5
mod = 10**9 + 7


fact = [0] * (m + 5)
fact_inv = [0] * (m + 5)
inv = [0] * (m + 5)

fact[0] = fact[1] = 1
fact_inv[0] = fact_inv[1] = 1
inv[1] = 1

for i in range(2, m + 5):
    fact[i] = fact[i - 1] * i % mod
    inv[i] = mod - inv[mod % i] * (mod // i) % mod
    fact_inv[i] = fact_inv[i - 1] * inv[i] % mod


def cmb(n, k, mod):
    return fact[n] * (fact_inv[k] * fact_inv[n - k] % mod) % mod


if k >= n - 1:
    print((cmb(2 * n - 1, n - 1, mod) % mod))
else:
    ans = 0
    for i in range(0, k + 1):
        ans += cmb(n, i, mod) * cmb(n - 1, n - i - 1, mod) % mod
        ans %= mod
    print(ans)
