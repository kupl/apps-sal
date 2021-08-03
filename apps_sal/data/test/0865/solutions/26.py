import numpy as np

N, T = map(int, input().split())
ABs = [tuple(map(int, input().split())) for _ in range(N)]

dp = np.zeros((N + 1, 2, T), np.int64)
for i, (A, B) in enumerate(ABs):
    dp[i + 1] = dp[i]
    dp[i + 1, 1] = np.maximum(dp[i, 0] + B, dp[i + 1, 1])
    dp[i + 1, :, A:] = np.maximum(dp[i, :, :-A] + B, dp[i + 1, :, A:])

print(np.max(dp[N]))
