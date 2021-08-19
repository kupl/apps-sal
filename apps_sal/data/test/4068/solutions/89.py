(n, m) = map(int, input().split())
oks = [True] * (n + 1)
for _ in range(m):
    a = int(input())
    oks[a] = False
mod = 1000000007
dp = [0] * (n + 1)
dp[0] = 1
if oks[1]:
    dp[1] = 1
for i in range(2, n + 1):
    if oks[i]:
        dp[i] = dp[i - 1] + dp[i - 2]
        dp[i] %= mod
print(dp[-1])
