n, a = list(map(int, input().split()))
x = list(map(int, input().split()))
MAX = 50 * n

dp = [[[0] * (MAX + 1) for _ in range(n + 1)] for _ in range(n + 1)]
dp[0][0][0] = 1

for i, e in enumerate(x, 1):
    for j in range(i):
        for k in range(MAX + 1):
            dp[i][j][k] += dp[i-1][j][k]

    for j in range(i):
        for k in range(MAX - e + 1):
            dp[i][j+1][k+e] += dp[i-1][j][k]

ans = 0
for cnt in range(1, n + 1):
    sm = cnt * a
    ans += dp[n][cnt][sm]

print(ans)

