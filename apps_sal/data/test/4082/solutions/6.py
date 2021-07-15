n = int(input())
a = list(map(int, input().split()))
dp = [1 for i in range(n)]
dpStart = [1 for i in range(n)]
for i in range(1, n):
    if a[i] > a[i - 1]:
        dp[i] = dp[i - 1] + 1
for i in range(n - 2, -1, -1):
    if a[i] < a[i + 1]:
        dpStart[i] = dpStart[i + 1] + 1
m = max(dp)
ans = m
for i in range(1, n - 1):
    # print(ans)
    if a[i - 1] < a[i + 1]:
        ans = max(ans, dp[i - 1] + dpStart[i + 1])

print(ans)
