import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(): return list(map(int, input().split()))
def ZIP(n): return list(zip(*(MAP() for _ in range(n))))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

L = input()

dp = [[0] * 2 for _ in range(len(L) + 1)]
dp[0][0] = 1

for i in range(len(L)):
    nd = int(L[i])
    ni = i + 1
    for a in range(2):
        for b in range(2):
            if a == b == 1:
                continue
            for k in range(2):
                nk = k

                if nk == 0:  # 未確定
                    if nd == 1 and a == b == 0:
                        nk = 1
                    if nd == 0 and a | b:  # 超える
                        continue

                dp[ni][nk] += dp[i][k]
                dp[ni][nk] %= mod

ans = dp[-1][0] + dp[-1][1]
print((ans % mod))
