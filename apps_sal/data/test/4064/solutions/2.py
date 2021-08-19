(n, h, l, r) = map(int, input().split())
a = list(map(int, input().split()))
dp = [[-1] * h for _ in range(n + 1)]
dp[0][0] = 0
for i in range(n):
    for j in range(h):
        if dp[i][j] < 0:
            continue
        dp[i + 1][(j + a[i]) % h] = max(dp[i + 1][(j + a[i]) % h], dp[i][j] + (l <= (j + a[i]) % h <= r))
        dp[i + 1][(j + a[i] - 1) % h] = max(dp[i + 1][(j + a[i] - 1) % h], dp[i][j] + (l <= (j + a[i] - 1) % h <= r))
print(max(dp[-1]))
