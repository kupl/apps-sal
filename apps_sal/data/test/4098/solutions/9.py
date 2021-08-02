n, k = map(int, input().split())
dp = [[0 for j in range(k + 1)] for i in range(n + 1)]
a = sorted([int(i) for i in input().split()])
cnt = [0 for i in range(n)]
for i in range(n):
    while i + cnt[i] < n and a[i + cnt[i]] - a[i] <= 5:
        cnt[i] += 1


for i in range(n):
    for j in range(k + 1):
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        if j + 1 <= k:
            dp[i + cnt[i]][j + 1] = max(dp[i + cnt[i]][j + 1], dp[i][j] + cnt[i])

print(dp[n][k])
