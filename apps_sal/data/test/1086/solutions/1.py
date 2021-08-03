h, w = list(map(int, input().split()))
a = [list(map(int, input().split()))for _ in range(h)]
b = [list(map(int, input().split()))for _ in range(h)]
c = [[abs(a[i][j] - b[i][j]) for j in range(w)]for i in range(h)]
dp = [[0] * (w + 1)for _ in range(h + 1)]
dp[0][1] = 1 << 12800
for i in range(1, h + 1):
    for j in range(1, w + 1):
        t = c[i - 1][j - 1]
        dp[i][j] = (dp[i][j - 1] << t) | (dp[i][j - 1] >> t) | (dp[i - 1][j] << t) | (dp[i - 1][j] >> t)
ans = 10**20
for i in range(25601):
    if dp[h][w] & (1 << i):
        ans = min(ans, abs(12800 - i))
print(ans)
