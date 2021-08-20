(n, k) = list(map(int, input().split()))
dp = [0] * (2 * n + 1)
for ii in range(1, n + 1):
    dp[ii + 1] = ii
    dp[ii + n] = n - ii + 1
r = 0
for ab in range(2, 2 * n + 1):
    cd = ab - k
    if cd > 1 and cd <= 2 * n:
        r += dp[ab] * dp[cd]
print(r)
