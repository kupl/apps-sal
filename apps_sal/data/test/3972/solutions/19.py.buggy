n = int(input())
if n == 1:
    print((1))
    return
mod = 10**9 + 7
dp = [0] * (n + 1)
S = [0] * (n + 1)
dp[0] = 1
dp[1] = 1
dp[2] = 1
S[0] = 1
for i in range(n):
    if i + 1 >= 3:
        dp[i + 1] = 2 * dp[i] - dp[i - 1] + dp[i - 2]
    dp[i + 1] %= mod
    S[i + 1] = S[i] + (n - 1) * dp[i]
    S[i + 1] %= mod
ans = S[n]
for i in range(1, n):
    ans += ((n - 1)**2) * dp[i - 1]
    ans %= mod
print(ans)
# print(S)
# print(dp)
