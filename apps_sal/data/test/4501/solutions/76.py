(N, A) = map(int, input().split())
x = list(map(int, input().split()))
maxX = max(max(x), A)
dp = [[[0 for _ in range(N * maxX + 1)] for _ in range(N + 1)] for _ in range(N + 1)]
dp[0][0][0] = 1
for i in range(N):
    for j in range(N + 1):
        for k in range(N * A + 1):
            if dp[i][j][k] == 0:
                continue
            dp[i + 1][j][k] += dp[i][j][k]
            dp[i + 1][j + 1][k + x[i]] += dp[i][j][k]
ans = 0
for i in range(1, N + 1):
    ans += dp[N][i][A * i]
print(ans)
