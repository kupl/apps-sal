n = int(input())
bn = bin(n)[2:]
dp = [[0] * 3 for i in range(len(bn) + 1)]
mod = 10**9 + 7
dp[len(bn)][0] = 1
for d in range(len(bn) - 1, -1, -1):
    if bn[len(bn) - 1 - d] == "1":
        dp[d][0] = dp[d + 1][0]
        dp[d][1] = dp[d + 1][0] + dp[d + 1][1]
        dp[d][2] = 2 * dp[d + 1][1] + 3 * dp[d + 1][2]
    else:
        dp[d][0] = dp[d + 1][0] + dp[d + 1][1]
        dp[d][1] = dp[d + 1][1]
        dp[d][2] = dp[d + 1][1] + 3 * dp[d + 1][2]
print((dp[0][0] + dp[0][1] + dp[0][2]) % mod)
