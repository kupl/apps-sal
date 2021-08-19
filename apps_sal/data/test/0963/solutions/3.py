import sys
#import time
from collections import deque, Counter, defaultdict
#from fractions import gcd
import bisect
import heapq
#import math
import itertools
import numpy as np
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
inf = 10**18
MOD = 1000000007
def ri(): return int(input())
def rs(): return input().strip()
def rl(): return list(map(int, input().split()))


mod = 998244353

n, k = rl()
ch = []
for i in range(k):
    ch.append(tuple(rl()))
dp = [0] * (n + 1)
dp[0] = 0
dp[1] = 1
for i in range(1, n):
    for e in ch:
        left = max(0, i - e[1])
        right = max(0, i - e[0] + 1)
        dp[i + 1] += dp[right] - dp[left]
    dp[i + 1] += dp[i]
    dp[i + 1] %= mod
print((dp[n] - dp[n - 1]) % mod)
