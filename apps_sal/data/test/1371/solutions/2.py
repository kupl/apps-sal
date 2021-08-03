N = int(input())
dp = [0] * 200000
dp[0] = 0
dp[1] = 0
dp[2] = 0
dp[3] = 1
for i in range(4, N + 1):
    dp[i] = dp[i - 1] + dp[i - 3]
print(dp[N] % (10**9 + 7))
