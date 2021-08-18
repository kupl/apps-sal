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
m = 2 * 10 ** 5
mod = 998244353
N, M, K = map(int, input().split())
ans = 0
A = [0] * (m + 5)
A_inv = [0] * (m + 5)
inv = [0] * (m + 5)

A[0] = A[1] = 1
A_inv[0] = A_inv[1] = 1
inv[1] = 1
for j in range(2, m + 5):
    A[j] = A[j - 1] * j % mod
    inv[j] = mod - inv[mod % j] * (mod // j) % mod
    A_inv[j] = A_inv[j - 1] * inv[j] % mod


def cmb(n, k, mod):
    return A[n] * (A_inv[k] * A_inv[n - k] % mod) % mod


for i in range(K + 1):
    ans = (ans + (cmb(N - 1, i, mod) * M % mod) * (pow(M - 1, N - 1 - i, mod)) % mod) % mod
print(ans)
