n, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
dp = [[0 for i in range(k + 1)]for j in range(n + 1)]
prev = [0 for i in range(n)]
for i in range(n):
    for j in range(i, -1, -1):
        if l[i] - l[j] <= 5:
            prev[i] = j
for i in range(k + 1):
    dp[0][i] = 0
for i in range(1, n + 1):
    for j in range(1, k + 1):
        # print(i,j,prev[i])
        dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j], dp[prev[i - 1]][j - 1] + i - prev[i - 1])
print(dp[n][k])
