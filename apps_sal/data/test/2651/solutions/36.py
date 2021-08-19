import sys
import heapq
import math
from itertools import zip_longest, permutations, combinations, combinations_with_replacement
from itertools import accumulate, dropwhile, takewhile, groupby
from functools import lru_cache
from copy import deepcopy
(N, M) = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
MOD = int(1000000000.0) + 7
xs = 0
for i in range(N):
    xs += i * X[i] % MOD - (N - i - 1) * X[i] % MOD + 2 * MOD
    xs %= MOD
ys = 0
for i in range(M):
    ys += i * Y[i] % MOD - (M - i - 1) * Y[i] % MOD + 2 * MOD
    ys %= MOD
print(xs * ys % MOD)
