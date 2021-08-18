import sys
import numpy as np


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


MOD = 998244353
N, S = lr()
A = lr()
dp = np.zeros(S + 1, np.int64)
answer = 0
for a in A:
    dp[0] += 1
    prev = dp.copy()
    dp[a:] += prev[:-a]
    dp %= MOD
    answer += dp[-1]

print((answer % MOD))
