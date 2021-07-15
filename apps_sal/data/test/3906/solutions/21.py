n, m = map(int,input().split())
dp = [0]*100001
dp[0], dp[1] = 1, 1
MOD =1000000007
for i in range(2,100001):
	dp[i] = (dp[i - 2] + dp[i - 1]) % MOD
print(2 * (dp[n] + dp[m] - 1) % MOD)
