(n, l, r) = map(int, input().split())
dp = [[0] * 3 for _ in range(n + 5)]
mod = 10 ** 9 + 7
rcnt = [0] * 3
(ll, rr) = (l // 3 + 1, r // 3)
for i in range(3):
    rcnt[i] += rr - ll
if l % 3 == 0:
    rcnt[0] += 1
    rcnt[1] += 1
    rcnt[2] += 1
elif l % 3 == 1:
    rcnt[1] += 1
    rcnt[2] += 1
else:
    rcnt[2] += 1
if r % 3 == 0:
    rcnt[0] += 1
elif r % 3 == 1:
    rcnt[0] += 1
    rcnt[1] += 1
else:
    rcnt[0] += 1
    rcnt[1] += 1
    rcnt[2] += 1
for i in range(3):
    dp[1][i] = rcnt[i] % mod
for i in range(2, n + 1):
    x = [dp[i - 1][0] * rcnt[0] % mod, dp[i - 1][2] * rcnt[1] % mod, dp[i - 1][1] * rcnt[2] % mod]
    y = [dp[i - 1][0] * rcnt[1] % mod, dp[i - 1][1] * rcnt[0] % mod, dp[i - 1][2] * rcnt[2] % mod]
    z = [dp[i - 1][0] * rcnt[2] % mod, dp[i - 1][1] * rcnt[1] % mod, dp[i - 1][2] * rcnt[0] % mod]
    dp[i][0] = sum(x) % mod
    dp[i][1] = sum(y) % mod
    dp[i][2] = sum(z) % mod
print(dp[n][0])
