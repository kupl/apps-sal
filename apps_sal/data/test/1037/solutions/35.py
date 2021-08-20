N = int(input())
As = list(map(int, input().split()))
dp = [[0] * (N - k + 1) for k in range(N + 1)]
s = 0
for (i, A) in sorted(enumerate(As), key=lambda t: t[1], reverse=True):
    s += 1
    for x in range(s + 1):
        y = s - x
        if x > 0 and y > 0:
            dp[x][y] = max(dp[x - 1][y] + A * (i - x + 1), dp[x][y - 1] + A * (N - y - i))
        elif x == 0:
            dp[x][y] = dp[x][y - 1] + A * (N - y - i)
        else:
            dp[x][y] = dp[x - 1][y] + A * (i - x + 1)
ans = max((dp[x][N - x] for x in range(N + 1)))
print(ans)
