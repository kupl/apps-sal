import sys
import numpy as np


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


MOD = 998244353
N, S = lr()
A = lr()
dp = np.zeros(S + 1, np.int64)
dp[0] = 1
for a in A:
    prev = dp.copy()
    dp[a:] += dp[:-a]
    dp += prev
    dp %= MOD

answer = dp[S]
print((answer % MOD))
