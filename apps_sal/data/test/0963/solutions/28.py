n, k= map(int, input().split())
lr = [tuple(map(int, input().split())) for i in range(k)]

MOD = 998244353

dp = [0] * n
dp[0] = 1

imos = [0] * n

for i in range(0, n):
	imos[i] += imos[i - 1]
	imos[i] %= MOD
	dp[i] += imos[i]
	dp[i] %= MOD
	for l, r in lr:
		if i + l < n:
			imos[i + l] += dp[i]
		if i + r + 1 < n:
			imos[i + r + 1] -= dp[i]
print(dp[n - 1])
