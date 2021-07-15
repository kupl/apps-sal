h, w = map(int, input().split())
a = [list(map(int, input().split())) for i in range(h)]
b = [list(map(int, input().split())) for i in range(h)]
dp = [[0] * (w + 1) for i in range(h + 1)]
dp[0][0] = 1 << ((h + w) * 80)
for i in range(h):
    for j in range(w):
        diff = abs(a[i][j] - b[i][j])
        dp[i + 1][j] |= (dp[i][j] << diff) | (dp[i][j] >> diff)
        dp[i][j + 1] |= (dp[i][j] << diff) | (dp[i][j] >> diff)
ans = float("inf")
for i in range((h + w) * 160):
    if dp[h][w - 1] & (1 << i):
        ans = min(ans, abs(i - ((h + w) * 80)))
print(ans)
