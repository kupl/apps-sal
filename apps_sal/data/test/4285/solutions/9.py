n = int(input())
seq = input()
dp = [0, 0]
ans = 0
mod = int(1e9 + 7)
pat = 1
for i in seq:
    if i == 'a':
        dp[0] = (dp[0] + pat) % mod
    elif i == 'b':
        dp[1] += dp[0]
        dp[1] %= mod
    elif i == 'c':
        ans = (ans + dp[1]) % mod
    else:
        ans = (3 * ans + dp[1]) % mod
        dp[1] = (3 * dp[1] + dp[0]) % mod
        dp[0] = (3 * dp[0] + pat) % mod
        pat = (3 * pat) % mod
print(ans)
