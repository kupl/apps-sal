n = int(input())
s = input()
ar = list(map(int, input().split()))
dp = [[0, 0, 0, 0] for i in range(n + 1)]
for i in range(1, n + 1):
    if s[i - 1] == 'h':
        dp[i][1] = dp[i - 1][1]
        dp[i][2] = dp[i - 1][2]
        dp[i][3] = dp[i - 1][3]
        dp[i][0] = dp[i - 1][0] + ar[i - 1]
    elif s[i - 1] == 'a':
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = min(dp[i - 1][0], ar[i - 1] + dp[i - 1][1])
        dp[i][2] = dp[i - 1][2]
        dp[i][3] = dp[i - 1][3]
    elif s[i - 1] == 'r':
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = dp[i - 1][1]
        dp[i][2] = min(dp[i - 1][1], ar[i - 1] + dp[i - 1][2])
        dp[i][3] = dp[i - 1][3]
    elif s[i - 1] == 'd':
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = dp[i - 1][1]
        dp[i][2] = dp[i - 1][2]
        dp[i][3] = min(dp[i - 1][2], ar[i - 1] + dp[i - 1][3])
    else:
        dp[i][1] = dp[i - 1][1]
        dp[i][2] = dp[i - 1][2]
        dp[i][3] = dp[i - 1][3]
        dp[i][0] = dp[i - 1][0]
print(dp[n][3])
