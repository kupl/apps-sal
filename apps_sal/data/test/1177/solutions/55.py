import numpy as np
mod = 998244353
N, S = list(map(int, input().split()))
A = [0] + list(map(int, input().split()))

dp = np.array([[0 for _ in range(S + 1)] for i in range(N + 1)])

for k in range(0, N):
    dp[k + 1, :] += (2 * dp[k, :] - dp[k - 1, :]) % mod
    if S > A[k + 1]:
        dp[k + 1, A[k + 1] + 1:] += (dp[k, 1:S - A[k + 1] + 1] - dp[k - 1, 1:S - A[k + 1] + 1]) % mod
    if A[k + 1] <= S:
        dp[k + 1, A[k + 1]] += k + 1

print(dp[N, S] % mod)
