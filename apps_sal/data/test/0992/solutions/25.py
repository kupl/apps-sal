import numpy as np

MOD = 998244353

N, S = map(int, input().split())
A = np.array(list(map(int, input().split())))

dp = np.zeros((N, S + 1))
dp[0, 0] = 2
if A[0] < S + 1:
	dp[0, A[0]] = 1

for i in range(1, N):
	dp[i, :] = (2 * dp[i - 1, :]) % MOD
	if A[i] > S:
		continue
	dp[i, A[i] : S + 1] += dp[i - 1, 0 : S - A[i] + 1]
	dp[i, :] %= MOD
print(int(dp[N - 1, S]))
