import numpy as np
import heapq
from heapq import heappush
from heapq import heappop
from heapq import heapify
import itertools
from bisect import insort_left
from bisect import bisect_left
from collections import deque
import math
import fractions
from collections import Counter
from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
INF = float("inf")
#d = defaultdict(int)
#d = defaultdict(list)
#N = int(input())
#A = list(map(int,input().split()))
#S = list(input())
# S.remove("\n")
#N,M = map(int,input().split())
#S,T = map(str,input().split())
#A = [int(input()) for _ in range(N)]
#S = [input() for _ in range(N)]
#A = [list(map(int,input().split())) for _ in range(N)]
n, k = map(int, input().split())
MOD = 10**9 + 7


def comb(n, k, mod):
    if n < 0 or k < 0 or n < k:
        return 0
    if n == 0 or k == 0:
        return 1
    k = k if k <= n - k else n - k
    x = 1
    y = 1
    for i in range(k):
        x = x * (n - i) % mod
        y = y * (i + 1) % mod
    return (x * pow(y, mod - 2, mod)) % mod


# こっちは計算量O(N)
fac = [1, 1]
inv = [0, 1]
finv = [1, 1]
for i in range(2, 2 * n + 1):
    fac.append(fac[-1] * i % MOD)
    inv.append(MOD - inv[MOD % i] * (MOD // i) % MOD)
    finv.append(finv[-1] * inv[-1] % MOD)


def comb_mod(n, r, m):
    if (n < 0 or r < 0 or n < r):
        return 0
    r = min(r, n - r)
    return fac[n] * finv[n - r] * finv[r] % m


if k >= n - 1:
    ans = comb_mod(2 * n - 1, n, MOD)
    print(ans % MOD)
elif k == 1:
    print(n * (n - 1) % MOD)
else:
    ans = 0
    for i in range(k + 1):
        ans += comb_mod(n - 1, i, MOD) * comb_mod(n, i, MOD)
    print(ans % MOD)
