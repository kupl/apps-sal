h, w = map(int, input().split())
a = [list(map(int, input().split())) for i in range(h)]
b = [list(map(int, input().split())) for i in range(h)]
grid = [[0 for i in range(w)] for j in range(h)]
for i in range(h):
    for j in range(w):
        grid[i][j] = abs(a[i][j] - b[i][j])
dp = [[0 for j in range(w)] for k in range(h)]
buf = (h + w) * 80
for i in range(h):
    for j in range(w):
        t = grid[i][j]
        if i == j == 0:
            dp[i][j] = 1 << buf + t | 1 << buf - t
        if j > 0:
            dp[i][j] = dp[i][j] | dp[i][j - 1] << t | dp[i][j - 1] >> t
        if i > 0:
            dp[i][j] = dp[i][j] | dp[i - 1][j] << t | dp[i - 1][j] >> t
for i in range(buf):
    if (dp[h - 1][w - 1] & 1 << buf + i) or (dp[h - 1][w - 1] & 1 << buf - i):
        print(i)
        return
