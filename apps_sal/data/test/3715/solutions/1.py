3

n = int(input())
a = list(map(int, input().split()))

dp = [[-1791791791] * 4 for i in range(n)]

dp[0][0] = 0
if a[0] & 1:
    dp[0][1] = 1
if a[0] & 2:
    dp[0][2] = 1

for i in range(1, n):
    dp[i][0] = max(dp[i - 1])
    for j in range(1, 3):
        if a[i] & j:
            dp[i][j] = max(dp[i - 1][:j] + dp[i - 1][j + 1:]) + 1

ans = max(dp[-1])
print(n - ans)

