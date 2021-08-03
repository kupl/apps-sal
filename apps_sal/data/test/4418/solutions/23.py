n = int(input())
a = list(map(int, input().split()))
dp = [0, 0, 0, 0, 0, 0]
for k in range(n):
    if a[k] == 4:
        dp[0] += 1
    elif a[k] == 8:
        dp[1] = min(dp[0], dp[1] + 1)
    elif a[k] == 15:
        dp[2] = min(dp[1], dp[2] + 1)
    elif a[k] == 16:
        dp[3] = min(dp[2], dp[3] + 1)
    elif a[k] == 23:
        dp[4] = min(dp[3], dp[4] + 1)
    else:
        dp[5] = min(dp[4], dp[5] + 1)

print(n - 6 * dp[5])
