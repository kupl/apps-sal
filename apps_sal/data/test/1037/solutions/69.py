n = int(input())
xs = list(enumerate(map(int, input().split())))
xs.sort(key=lambda x: x[1])
xs.reverse()
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    (j, a) = xs[i - 1]
    for x in range(0, i + 1):
        y = i - x
        if x == 0:
            dp[x][y] = dp[x][y - 1] + a * (n - y - j)
        elif y == 0:
            dp[x][y] = dp[x - 1][y] + a * (j - x + 1)
        else:
            dp[x][y] = max(dp[x][y - 1] + a * (n - y - j), dp[x - 1][y] + a * (j - x + 1))
print(max([dp[i][n - i] for i in range(n + 1)]))
