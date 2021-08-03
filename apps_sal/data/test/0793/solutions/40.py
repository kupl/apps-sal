import numpy as np

N, M = map(int, input().split())
MOD = 1e9 + 7
S = np.array(input().split())
T = np.array(input().split())

dp = np.zeros((N + 1, M + 1))
dp[0] = 1

for n in range(1, N + 1):
    same = (T == S[n - 1])
    dp[n, 1:][same] = dp[n - 1, :-1][same]
    dp[n] = (dp[n].cumsum() + dp[n - 1]) % MOD

print(int(dp[N, M]))
