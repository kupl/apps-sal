N = int(input())
dp = [0] * 200000
dp[0] = 1
dp[1] = 0
dp[2] = 0
dp[3] = 1
for i in range(4, N + 1):
    for j in range(i - 2):
        dp[i] += dp[j]
print(dp[N] % (10 ** 9 + 7))
