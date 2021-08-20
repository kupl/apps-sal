(h, w) = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
b = [list(map(int, input().split())) for _ in range(h)]
dp = [w * [0] for _ in range(h)]
dp[0][0] = 1 << 80 + (a[0][0] - b[0][0]) | 1 << 80 + (b[0][0] - a[0][0])
for i in range(h):
    for j in range(w):
        if i != 0:
            dp[i][j] |= dp[i - 1][j] << 80 + (a[i][j] - b[i][j])
            dp[i][j] |= dp[i - 1][j] << 80 + (b[i][j] - a[i][j])
        if j != 0:
            dp[i][j] |= dp[i][j - 1] << 80 + (a[i][j] - b[i][j])
            dp[i][j] |= dp[i][j - 1] << 80 + (b[i][j] - a[i][j])
ans = 1 << 50000
for i in range(50000):
    if dp[h - 1][w - 1] & 1 << i:
        ans = min(abs(i - (h + w - 1) * 80), ans)
print(ans)
