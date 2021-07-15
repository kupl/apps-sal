n = int(input())

MOD = 10 ** 9 + 7

k = len(bin(n)) - 2

dp = [[0, 0, 0] for _ in range(k + 1)]

dp[0][0] = 1

for i in range(k):
    if (n >> (k - 1 - i)) & 1:
        dp[i+1][0] = dp[i][0]
        dp[i+1][1] = dp[i][0] + dp[i][1]
        dp[i+1][2] = dp[i][1] * 2 + dp[i][2] * 3
    else:
        dp[i+1][0] = dp[i][0] + dp[i][1]
        dp[i+1][1] = dp[i][1]
        dp[i+1][2] = dp[i][1] + dp[i][2] * 3
    map(lambda x:x%MOD, dp[k])

print(sum(dp[k]) % MOD)
