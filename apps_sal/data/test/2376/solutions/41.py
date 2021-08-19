(N, W) = list(map(int, input().split()))
ls = []
for i in range(N):
    (w, v) = list(map(int, input().split()))
    ls += [[w, v]]
w1 = ls[0][0]
for i in range(N):
    ls[i][0] -= w1
ans = 0
M = 3 * N
dp = [[-1] * (M + 1) for i in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    (w, v) = ls[i]
    for h in range(N, 0, -1):
        for j in range(M, -1, -1):
            if j - w >= 0 and dp[h - 1][j - w] != -1:
                dp[h][j] = max(dp[h][j], dp[h - 1][j - w] + v)
for i in range(1, N + 1):
    B = i * w1
    m = 0
    for j in range(M + 1):
        if B + j <= W:
            m = max(m, dp[i][j])
    if ans < m:
        ans = m
print(ans)
