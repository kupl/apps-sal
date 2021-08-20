s = input()
l = len(s)
dp = [4 * [0] for _ in range(l + 1)]
dp[0][0] = 1
for i in range(1, l + 1):
    si = s[i - 1]
    if si == '?':
        dp[i][0] = dp[i - 1][0] * 3
        dp[i][1] = dp[i - 1][1] * 3
        dp[i][2] = dp[i - 1][2] * 3
        dp[i][3] = dp[i - 1][3] * 3
    else:
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = dp[i - 1][1]
        dp[i][2] = dp[i - 1][2]
        dp[i][3] = dp[i - 1][3]
    if si == 'A':
        dp[i][1] = dp[i - 1][0] + dp[i][1]
    elif si == 'B':
        dp[i][2] = dp[i - 1][1] + dp[i][2]
    elif si == 'C':
        dp[i][3] = dp[i - 1][2] + dp[i][3]
    else:
        dp[i][1] = dp[i - 1][0] + dp[i][1]
        dp[i][2] = dp[i - 1][1] + dp[i][2]
        dp[i][3] = dp[i - 1][2] + dp[i][3]
    for j in range(4):
        dp[i][j] = dp[i][j] % 1000000007
print(int(dp[-1][-1]))
