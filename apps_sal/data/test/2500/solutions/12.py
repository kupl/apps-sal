n = int(input())
x = n.bit_length()
dp = [[0] * 3 for i in range(x)]
dp[-1][0] = 1
dp[-1][1] = 1
mod = 10 ** 9 + 7
for i in range(x - 2, -1, -1):
    if n >> i & 1:
        dp[i][0] = dp[i + 1][0] % mod
        dp[i][1] = (dp[i + 1][0] + dp[i + 1][1]) % mod
        dp[i][2] = (dp[i + 1][2] * 3 + dp[i + 1][1] * 2) % mod
    else:
        dp[i][0] = (dp[i + 1][0] + dp[i + 1][1]) % mod
        dp[i][1] = dp[i + 1][1] % mod
        dp[i][2] = (dp[i + 1][2] * 3 + dp[i + 1][1]) % mod
print(sum(dp[0]) % mod)
