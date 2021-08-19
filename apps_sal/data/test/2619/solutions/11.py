input = __import__('sys').stdin.readline
(n, q, c) = map(int, input().split())
dp = [[[0 for i in range(101)] for j in range(101)] for k in range(c + 1)]
for i in range(n):
    (x, y, s) = map(int, input().split())
    dp[s][x][y] += 1
for i in range(c + 1):
    for j in range(1, 101):
        for k in range(1, 101):
            dp[i][j][k] += dp[i][j - 1][k] + dp[i][j][k - 1] - dp[i][j - 1][k - 1]
for _ in range(q):
    (t, x1, y1, x2, y2) = map(int, input().split())
    ans = 0
    for i in range(c + 1):
        bright = (i + t) % (c + 1)
        amt = dp[i][x2][y2] - dp[i][x1 - 1][y2] - dp[i][x2][y1 - 1] + dp[i][x1 - 1][y1 - 1]
        ans += bright * amt
    print(ans)
