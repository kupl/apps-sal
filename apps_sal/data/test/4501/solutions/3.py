n, a = list(map(int, input().split()))
x = list(map(int, input().split()))

dp = [[[0] * (50 * (n + 10)) for _ in range(n + 10)] for _ in range(n + 10)]
dp[0][0][0] = 1

for i in range(n):
    for use in range(n):
        for total in range(n * a):
            if dp[i][use][total]:
                dp[i + 1][use][total] += dp[i][use][total]
                dp[i + 1][use + 1][total + x[i]] += dp[i][use][total]

ans = 0
for i in range(1, n + 1):
    ans += dp[n][i][a * i]

print(ans)

