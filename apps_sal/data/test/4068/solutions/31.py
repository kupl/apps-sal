n, m = map(int, input().split())
mod = pow(10, 9) + 7
dp = [0] * (n + 5)
for _ in range(m):
    a = int(input())
    dp[a] = -1
dp[0] = 1
for i in range(n):
    if not dp[i] == -1:
        dp[i] %= mod
    else:
        continue
    if not dp[i + 1] == -1:
        dp[i + 1] += dp[i]
    if not dp[i + 2] == -1:
        dp[i + 2] += dp[i]
ans = dp[n] % mod
print(ans)
