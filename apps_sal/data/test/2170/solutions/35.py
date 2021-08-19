import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
from itertools import accumulate, permutations, combinations, product, groupby, combinations_with_replacement
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from heapq import heappush, heappop
from functools import reduce


def input():
    return sys.stdin.readline().strip()


def INT():
    return int(input())


def MAP():
    return list(map(int, input().split()))


def LIST():
    return list(map(int, input().split()))


def ZIP(n):
    return list(zip(*(MAP() for _ in range(n))))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7
(N, M) = MAP()
lim = M + 10
fact = [1] * (lim + 1)
fact_inv = [1] * (lim + 1)
for n in range(1, lim + 1):
    fact[n] = fact[n - 1] * n % mod
fact_inv[lim] = pow(fact[lim], mod - 2, mod)
for n in range(lim, 0, -1):
    fact_inv[n - 1] = n * fact_inv[n] % mod


def C(n, r):
    return fact[n] * fact_inv[r] % mod * fact_inv[n - r] % mod


def P(n, r):
    return fact[n] * fact_inv[n - r] % mod


ans = 0
for k in range(N + 1):
    ans += (-1) ** (k % 2) * C(N, k) * P(M - k, N - k)
    ans %= mod
ans *= P(M, N)
print(ans % mod)
