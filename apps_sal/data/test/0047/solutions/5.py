(N, X) = list(map(int, input().split()))
a_list = list(map(int, input().split()))
dp = [[0] * 5 for _ in range(303030)]
for i in range(N):
    a = a_list[i]
    dp[i + 1][0] = 0
    dp[i + 1][1] = max(dp[i][1] + a, dp[i + 1][0])
    dp[i + 1][2] = max(dp[i][2] + a * X, dp[i + 1][1])
    dp[i + 1][3] = max(dp[i][3] + a, dp[i + 1][2])
    dp[i + 1][4] = max(dp[i][4], dp[i + 1][3])
print(dp[N][4])
