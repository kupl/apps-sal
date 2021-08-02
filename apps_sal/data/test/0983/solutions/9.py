n, p, q, r = list(map(int, input().split()))
a = list(map(int, input().split()))[::-1]

INF = -10 ** 30

answer = INF
dp = [INF, INF, INF]

for i in range(n):
    dp[0] = max(dp[0], r * a[i])
    dp[1] = max(dp[1], q * a[i] + dp[0])
    dp[2] = max(dp[2], p * a[i] + dp[1])
    answer = max(answer, dp[2])

print(answer)
