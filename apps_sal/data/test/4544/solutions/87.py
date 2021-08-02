N = int(input())
a = list(map(int, input().strip().split()))

dp = [0 for n in range(max(a) + 1)]
for n in range(N):
    dp[a[n]] += 1

ans = 0
if len(dp) == 1:
    ans = dp[0]
else:
    for n in range(1, len(dp) - 1):
        ans = max(ans, dp[n - 1] + dp[n] + dp[n + 1])

print(ans)
