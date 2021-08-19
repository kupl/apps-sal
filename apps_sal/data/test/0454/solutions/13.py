import os
import sys
import numpy as np
if os.getenv('LOCAL'):
    sys.stdin = open('_in.txt', 'r')
sys.setrecursionlimit(2147483647)
INF = float('inf')
IINF = 10 ** 18
MOD = 10 ** 9 + 7
(N, K) = list(map(int, sys.stdin.readline().split()))
dp = np.zeros((N + 1, K + 1, N + 1), dtype=int)
dp[0, 0, 0] = 1
for i in range(N):
    for a in range(N + 1):
        k = np.arange(K + 1)
        if a == 0:
            dp[i + 1, :, a] += dp[i, :, a]
        else:
            dp[i + 1, a * 2:, a] += dp[i, :-(a * 2), a]
        if a * 2 - 2 == 0:
            dp[i + 1, :, a - 1] += dp[i, :, a] * a ** 2
        elif a * 2 - 2 > 0:
            dp[i + 1, a * 2 - 2:, a - 1] += dp[i, :-(a * 2 - 2), a] * a ** 2
        if a > 0:
            dp[i + 1, a * 2:, a] += dp[i, :-(a * 2), a] * a * 2
        if a + 1 < N:
            dp[i + 1, a * 2 + 2:, a + 1] += dp[i, :-(a * 2 + 2), a]
    dp[i + 1] %= MOD
print(dp[-1][K][0] % MOD)
