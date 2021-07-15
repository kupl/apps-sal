n = int(input())
a = list(map(int, input().split()))

ret = 0

if n % 2 == 0:
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0] = a[0]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] if i % 2 == 1 else dp[i-1][0] + a[i]
        dp[i][1] = dp[i - 1][1] if i % 2 == 0 \
            else max(dp[i-2][0], dp[i-2][1]) + a[i]
    ret = max(dp[-1])
else:
    dp = [[0] * 3 for _ in range(n)]
    dp[0][0] = a[0]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] if i % 2 == 1 else dp[i-1][0] + a[i]
        dp[i][1] = dp[i - 1][1] if i % 2 == 0 \
            else max(dp[i-2][0], dp[i-2][1]) + a[i]
        dp[i][2] = dp[i - 1][1] if i % 2 == 1 \
            else max(dp[i-3][0], dp[i-2][1], dp[i-2][2]) + a[i]
    ret = max(dp[-1][1], dp[-1][2], dp[-2][0])

print(ret)

