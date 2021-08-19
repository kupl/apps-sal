(N, A) = map(int, input().split())
x = list(map(int, input().split()))
maxint = 50 * N
dp = [[[0] * (maxint + 1) for _ in range(N + 1)] for _ in range(N + 1)]
dp[0][0][0] = 1
for (xi, xe) in enumerate(x, 1):
    for j in range(xi + 1):
        for k in range(maxint + 1):
            dp[xi][j][k] = dp[xi - 1][j][k]
            if j >= 0 and k >= xe:
                dp[xi][j][k] += dp[xi - 1][j - 1][k - xe]
res = 0
for i in range(1, N + 1):
    res += dp[N][i][i * A]
print(res)
