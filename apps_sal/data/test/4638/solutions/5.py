def I(): return list(map(int, input().split()))


n, c = I()
a = I()
b = I()
dp = [[0, 0] for i in range(300000)]
dp[1][0] = a[0]
dp[1][1] = c + b[0]

for i in range(2, n):
    dp[i][0] = min(dp[i - 1][0] + a[i - 1], dp[i - 1][1] + a[i - 1])
    dp[i][1] = min(dp[i - 1][0] + c + b[i - 1], dp[i - 1][1] + b[i - 1])
for i in range(n):
    print(min(dp[i][0], dp[i][1]), end=' ')
