import sys

import numpy as np


def input(): return sys.stdin.readline().rstrip()


MOD = 998244353

N, S = list(map(int, input().split()))
A = list(map(int, input().split()))

dp = np.zeros(S + 1, np.int64)
dp[0] = 1
for a in A:
    f = 2 * dp
    f[a:] += dp[:-a]
    f %= MOD
    dp = f

print((dp[S]))
