(n, m, k) = map(int, input().split())
col = list(map(int, input().split()))
p = []
for i in range(n):
    p.append(list(map(int, input().split())))
dp = [[[float('inf')] * m for i in range(k + 1)] for i in range(n)]
if col[0] == 0:
    for i in range(m):
        dp[0][1][i] = p[0][i]
else:
    dp[0][1][col[0] - 1] = 0
for i in range(1, n):
    for j in range(1, k + 1):
        if j == 1:
            if col[i]:
                dp[i][j][col[i] - 1] = dp[i - 1][j][col[i] - 1]
            else:
                for c in range(m):
                    dp[i][j][c] = dp[i - 1][j][c] + p[i][c]
        elif col[i]:
            x = dp[i - 1][j][col[i] - 1]
            for t in range(m):
                if t != col[i] - 1:
                    x = min(x, dp[i - 1][j - 1][t])
            dp[i][j][col[i] - 1] = x
        else:
            for c in range(m):
                x = dp[i - 1][j][c]
                for t in range(m):
                    if t != c:
                        x = min(x, dp[i - 1][j - 1][t])
                dp[i][j][c] = x + p[i][c]
ans = min(dp[-1][-1])
if ans != float('inf'):
    print(ans)
else:
    print(-1)
