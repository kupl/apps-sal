S = list(input())
mod = 10 ** 9 + 7
n = len(S)
dp = [[0] * 4 for _ in range(n)]
dp[-1][0] = 1
for (i, s) in enumerate(S):
    if s == '?':
        dp[i][0] = dp[i - 1][0] * 3 % mod
        dp[i][1] = (dp[i - 1][0] + dp[i - 1][1] * 3) % mod
        dp[i][2] = (dp[i - 1][1] + dp[i - 1][2] * 3) % mod
        dp[i][3] = (dp[i - 1][2] + dp[i - 1][3] * 3) % mod
    elif s == 'A':
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = (dp[i - 1][1] + dp[i - 1][0]) % mod
        dp[i][2] = dp[i - 1][2]
        dp[i][3] = dp[i - 1][3]
    elif s == 'B':
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = dp[i - 1][1]
        dp[i][2] = (dp[i - 1][1] + dp[i - 1][2]) % mod
        dp[i][3] = dp[i - 1][3]
    else:
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = dp[i - 1][1]
        dp[i][2] = dp[i - 1][2]
        dp[i][3] = (dp[i - 1][3] + dp[i - 1][2]) % mod
print(dp[-1][-1])
