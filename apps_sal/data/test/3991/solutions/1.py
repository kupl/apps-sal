n = int(input())
x = sorted(map(int, input().split()))
mod = 10 ** 9 + 7
(ans, deg) = (0, 1)
dp = [0] * n
for i in range(1, n):
    deg = (deg << 1) % mod
    dp[i] = (2 * dp[i - 1] + (x[i] - x[i - 1]) * (deg - 1)) % mod
    ans = (ans + dp[i]) % mod
print(ans)
