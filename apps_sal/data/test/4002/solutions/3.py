n, m, k = list(map(int, input().split()))
mat = [list(map(int, input().split())) for i in range(n)]
inf = 1 << 30
modulars = [[-inf] * (k) for i in range(n)]

for index in range(n):
    a = mat[index]
    dp = [[[-inf] * k for i in range(m // 2 + 1)]for _ in range(m + 1)]
    dp[0][0][0] = 0
    for i in range(1, m + 1):
        v = a[i - 1]
        for picked in range(m // 2 + 1):
            for mod in range(k):
                if picked >= 1:
                    dp[i][picked][mod] = max(dp[i][picked][mod], dp[i - 1][picked][mod], dp[i - 1][picked - 1][(mod - v) % k] + v)
                else:
                    dp[i][picked][mod] = max(dp[i][picked][mod], dp[i - 1][picked][mod])

    for mod in range(k):
        modulars[index][mod] = max(dp[m][picked][mod]
                                   for picked in range(m // 2 + 1))

dp = [[-inf] * (k) for i in range(n + 1)]
dp[0][0] = 0
for i in range(1, n + 1):
    for mod in range(k):
        dp[i][mod] = max(dp[i - 1][(mod - prevmod) % k] +
                         modulars[i - 1][prevmod]for prevmod in range(k))

ans = dp[n][0]
print(ans)
