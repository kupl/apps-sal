(n, m) = map(int, input().split())
a = [False] * (n + 1)
for i in range(m):
    A = int(input())
    a[A] = True
mod = 10 ** 9 + 7
dp = [0] * (n + 1)
if not a[1]:
    dp[1] = 1
if n > 1:
    if not a[2]:
        dp[2] = dp[1] + 1
for i in range(3, n + 1):
    if not a[i - 2]:
        dp[i] += dp[i - 2]
        dp[i] %= mod
    if not a[i - 1]:
        dp[i] += dp[i - 1]
        dp[i] %= mod
    if a[i]:
        dp[i] = 0
print(dp[n] % mod)
