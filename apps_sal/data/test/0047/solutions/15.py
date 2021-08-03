def printarr(dp):
    for i in dp:
        print(*i)


n, m = list(map(int, input().split()))
a = [0] + list(map(int, input().split()))
dp = [[0, 0, 0] for i in range(n + 1)]
ma = -1
for i in range(1, n + 1):
    dp[i][0] = max(dp[i - 1][0] + a[i], 0)
    dp[i][1] = max(dp[i - 1][1] + a[i] * m, dp[i - 1][0] + a[i] * m)
    dp[i][2] = max(dp[i - 1][2] + a[i], a[i] + dp[i - 1][1])
    ma = max(dp[i][0], dp[i][1], dp[i][2], ma)
# printarr(dp)
print(ma)
