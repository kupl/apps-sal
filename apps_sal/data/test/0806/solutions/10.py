(n, l, r) = list(map(int, input().split()))
mod = 10 ** 9 + 7
dp = [[0 for j in range(3)] for _ in range(n + 10)]
dp[0][0] = 1
m0 = r // 3
m1 = r // 3
m2 = r // 3
if r % 3 == 1:
    m1 += 1
elif r % 3 == 2:
    m1 += 1
    m2 += 1
l -= 1
m0 -= l // 3
m1 -= l // 3
m2 -= l // 3
if l % 3 == 1:
    m1 -= 1
elif l % 3 == 2:
    m1 -= 1
    m2 -= 1
for i in range(n):
    dp[i + 1][0] += dp[i][0] * m0
    dp[i + 1][1] += dp[i][0] * m1
    dp[i + 1][2] += dp[i][0] * m2
    dp[i + 1][1] += dp[i][1] * m0
    dp[i + 1][2] += dp[i][1] * m1
    dp[i + 1][0] += dp[i][1] * m2
    dp[i + 1][2] += dp[i][2] * m0
    dp[i + 1][0] += dp[i][2] * m1
    dp[i + 1][1] += dp[i][2] * m2
    dp[i + 1][0] %= mod
    dp[i + 1][1] %= mod
    dp[i + 1][2] %= mod
print(dp[n][0])
