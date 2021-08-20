n = int(input())
a = list(map(int, input().split()))
l = []
for (i, x) in enumerate(a):
    l.append([x, i])
l.sort(reverse=True)
cnt = 1
dp = [[0] * (n + 1) for _ in range(n + 1)]
for (i, j) in l:
    for x in range(cnt + 1):
        if x == 0:
            dp[x][cnt - x] = dp[x][cnt - x - 1] + i * (n - 1 - (cnt - x - 1) - j)
        elif x == cnt:
            dp[x][cnt - x] = dp[x - 1][cnt - x] + i * (j - x + 1)
        else:
            dp[x][cnt - x] = max(dp[x - 1][cnt - x] + i * (j - x + 1), dp[x][cnt - x - 1] + i * (n - 1 - (cnt - x - 1) - j))
    cnt += 1
ans = 0
for i in range(n + 1):
    ans = max(ans, dp[i][n - i])
print(ans)
