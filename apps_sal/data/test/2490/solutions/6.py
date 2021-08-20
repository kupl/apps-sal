S = input()
L = len(S)
dp = [[0 for _ in range(L + 1)] for over in range(2)]
dp[0][0] = 0
dp[1][0] = 1
for (j, s) in enumerate(S, 1):
    n = int(s)
    dp[0][j] = min(dp[0][j - 1] + n, dp[1][j - 1] + (10 - n))
    dp[1][j] = min(dp[0][j - 1] + (n + 1), dp[1][j - 1] + (10 - n - 1))
print(dp[0][-1])
