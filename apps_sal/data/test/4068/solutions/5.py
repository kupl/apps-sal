(n, m) = map(int, input().split())
broken = [False] * (n + 1)
for _ in range(m):
    i = int(input())
    broken[i] = True
dp = [0] * (n + 1)
dp[0] = 1
mod = 1000000007
for i in range(1, n + 1):
    if broken[i]:
        continue
    if i == 1:
        dp[1] = 1
        continue
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n] % mod)
