import numpy as np

MOD = 998244353

N, S = list(map(int, input().split()))
As = list(map(int, input().split()))

dp = np.zeros((N + 1, S + 1), np.int64)
dp[:, 0] = 1
dp[1, 0] = 3
if As[0] <= S:
    dp[1, As[0]] = 1
for i in range(1, N):
    A = As[i]
    dp[i + 1] += 2 * dp[i] - dp[i - 1]
    dp[i + 1, A:] += dp[i, :-A] - dp[i - 1, :-A]
    dp[i + 1] %= MOD

print((dp[N, S]))
