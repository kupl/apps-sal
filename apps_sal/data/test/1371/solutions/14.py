S = int(input())
mod = 10**9 + 7
dp = [0] * (S + 1)
dp[0] = 1
x = 0
for i in range(1, S + 1, 1):
    if i >= 3:
        x += dp[i - 3]
        x %= mod
    dp[i] = x
ans = dp[S]
print(ans % mod)
