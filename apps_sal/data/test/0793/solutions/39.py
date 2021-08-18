import numpy as np
MOD = 10**9 + 7
N, M = list(map(int, input().split()))
S = np.array(input().split(), dtype=np.int32)
T = np.array(input().split(), dtype=np.int32)

dp = np.zeros((N + 1, M + 1), dtype=np.int64)
dp[0] = 1

for n in range(1, N + 1):
    same = (T == S[n - 1])
    dp[n, 1:][same] = dp[n - 1, :-1][same]
    dp[n] = (dp[n].cumsum() + dp[n - 1]) % MOD

answer = dp[N, M]
print(answer)
