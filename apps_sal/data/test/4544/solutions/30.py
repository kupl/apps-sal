n = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(max(a) + 1)]
for i in range(n):
    dp[a[i]] += 1
ans = 0
if len(dp) == 1:
    ans = dp[0]
else:
    for i in range(1, len(dp) - 1):
        ans = max(ans, dp[i - 1] + dp[i] + dp[i + 1])
print(ans)
