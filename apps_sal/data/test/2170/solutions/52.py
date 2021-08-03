from decimal import Decimal
from copy import deepcopy
import heapq
from heapq import heappush
from heapq import heappop
from heapq import heapify
import itertools
from bisect import insort_left
from bisect import bisect_right
from bisect import bisect_left
from collections import deque
import math
import fractions
from collections import Counter
from collections import defaultdict
from itertools import combinations
from itertools import permutations
from itertools import accumulate
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
alf = list("abcdefghijklmnopqrstuvwxyz")
ALF = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
#import numpy as np
INF = float("inf")
#d = defaultdict(int)
#d = defaultdict(list)
N, M = list(map(int, input().split()))
fac = [1, 1]
inv = [0, 1]
finv = [1, 1]
MOD = 10**9 + 7
for i in range(2, M + 2):
    fac.append(fac[-1] * i % MOD)
    inv.append(MOD - inv[MOD % i] * (MOD // i) % MOD)
    finv.append(finv[-1] * inv[-1] % MOD)


def comb_mod(n, r, m):  # nCr mod m
    if (n < 0 or r < 0 or n < r):
        return 0
    r = min(r, n - r)
    return fac[n] * finv[n - r] * finv[r] % m


def chofuku(n, r):  # nHr mod MOD の計算
    return comb_mod(n + r - 1, r)


def nPr(n, r, m):  # nPr mod MOD の計算
    return fac[n] * finv[n - r] % m


ans = 0
for i in range(1, N + 1):
    if i % 2 == 1:
        flag = 1
    else:
        flag = -1
    s = flag * comb_mod(N, i, MOD) * nPr(M - i, N - i, MOD)
    ans += s
    if ans > MOD:
        ans %= MOD
ans1 = 1
for i in range(N):
    ans1 *= (M - i)
    ans1 %= MOD
ans2 = (ans1 * ans1) % MOD
ans3 = (ans * nPr(M, N, MOD)) % MOD
print(((ans2 - ans3) % MOD))
