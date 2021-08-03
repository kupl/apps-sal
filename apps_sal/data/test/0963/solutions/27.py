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
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(): return list(map(int, input().split()))
def ZIP(n): return list(zip(*(MAP() for _ in range(n))))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 998244353

N, K = MAP()
LR = [LIST() for _ in range(K)]
dp = [0] * (N + 1)
dp_acc = [0] * (N + 1)
dp[1] = 1
dp_acc[1] = 1

for i in range(2, N + 1):
    for L, R in LR:
        l = max(0, i - R - 1)
        r = max(0, i - L)
        dp[i] += dp_acc[r] - dp_acc[l]
        dp[i] %= mod
    dp_acc[i] = dp_acc[i - 1] + dp[i]
    dp_acc[i] %= mod

print((dp[-1]))
