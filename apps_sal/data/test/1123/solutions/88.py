# 解説AC
mod = 10 ** 9 + 7
n, k = list(map(int, input().split()))
dp = [-1] * (k + 1)
ans = 0
for i in range(k, 0, -1):
    dp[i] = pow(k // i, n, mod)
    t = 0
    t += 2 * i
    while t <= k:
        dp[i] -= dp[t]
        dp[i] %= mod
        t += i
    ans += i * dp[i]
    ans %= mod
print(ans)

