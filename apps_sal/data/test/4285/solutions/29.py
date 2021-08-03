n = int(input())
s = input()

dp = [[0, 0, 0] for _ in range(n)]
dp2 = [[0, 0, 0] for _ in range(n)]
prev = [0, 0, 0]
free = 0

mod = 1000000007
for i in range(n):
    if i > 0:
        dp[i] = dp[i - 1].copy()
    if s[i] == 'a':
        dp[i][0] += 1
    if s[i] == 'b':
        dp[i][1] += dp[i][0]
        if dp[i][1] >= mod:
            dp[i][1] -= mod
    if s[i] == 'c':
        dp[i][2] += dp[i][1]
        if dp[i][2] >= mod:
            dp[i][2] -= mod
    if s[i] == '?':
        free += 1

for i in reversed(range(0, n)):
    if i + 1 < n:
        dp2[i] = dp2[i + 1].copy()
    if s[i] == 'c':
        dp2[i][0] += 1
    if s[i] == 'b':
        dp2[i][1] += dp2[i][0]
        if dp2[i][1] >= mod:
            dp2[i][1] -= mod
    if s[i] == 'a':
        dp2[i][2] += dp2[i][1]
        if dp2[i][2] >= mod:
            dp2[i][2] -= mod

ans = dp[n - 1][2] * pow(3, free, mod) % mod
ans += (free * (free - 1) * (free - 2) // 6) * pow(3, mod - 1 + free - 3, mod) % mod
before, after = 0, free
for i in range(n):
    if s[i] == '?':
        mul = pow(3, free - 1, mod)
        ans += mul * (dp[i][0] * dp2[i][0] + dp2[i][1] + dp[i][1]) % mod
        before += 1
        after -= 1
    if s[i] == 'a':
        ans += pow(3, mod - 1 + free - 2, mod) * (after * (after - 1) // 2) % mod
    if s[i] == 'b':
        ans += pow(3, mod - 1 + free - 2, mod) * (after * before) % mod
    if s[i] == 'c':
        ans += pow(3, mod - 1 + free - 2, mod) * (before * (before - 1) // 2) % mod
    if ans >= mod:
        ans %= mod
print(ans % mod)
