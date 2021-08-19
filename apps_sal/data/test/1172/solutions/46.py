S = list(input())
n = len(S)
mod = 10 ** 9 + 7
dp = [[0] * 4 for i in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1):
    if S[i - 1] == 'A':
        dp[i][0] = dp[i - 1][0] % mod
        dp[i][1] = (dp[i - 1][0] + dp[i - 1][1]) % mod
        dp[i][2] = dp[i - 1][2] % mod
        dp[i][3] = dp[i - 1][3] % mod
    elif S[i - 1] == 'B':
        dp[i][0] = dp[i - 1][0] % mod
        dp[i][1] = dp[i - 1][1] % mod
        dp[i][2] = (dp[i - 1][1] + dp[i - 1][2]) % mod
        dp[i][3] = dp[i - 1][3] % mod
    elif S[i - 1] == 'C':
        dp[i][0] = dp[i - 1][0] % mod
        dp[i][1] = dp[i - 1][1] % mod
        dp[i][2] = dp[i - 1][2] % mod
        dp[i][3] = (dp[i - 1][2] + dp[i - 1][3]) % mod
    else:
        dp[i][0] = dp[i - 1][0] * 3 % mod
        dp[i][1] = (dp[i - 1][0] + dp[i - 1][1] * 3) % mod
        dp[i][2] = (dp[i - 1][1] + dp[i - 1][2] * 3) % mod
        dp[i][3] = (dp[i - 1][2] + dp[i - 1][3] * 3) % mod
print(dp[n][3])
