from sys import stdin
n, l, r = list(map(int, stdin.readline().strip().split()))
dp = [[0 for i in range(3)]for j in range(n)]
x = l // 3
if l % 3 != 0:
    x += 1
y = 3 * x
z = 0

for i in range(l, y + 1):
    z += 1
    if i % 3 == 0:
        dp[0][0] += 1
    if i % 3 == 1:
        dp[0][1] += 1
    if i % 3 == 2:
        dp[0][2] += 1
x = r // 3
y = 3 * x

for i in range(y + 1, r + 1):
    z += 1
    if i % 3 == 0:
        dp[0][0] += 1
    if i % 3 == 1:
        dp[0][1] += 1
    if i % 3 == 2:
        dp[0][2] += 1
x = (r - l + 1 - z) // 3
mod = 10**9 + 7
dp[0][0] += x
dp[0][1] += x
dp[0][2] += x
for i in range(1, n):
    dp[i][0] = ((dp[0][0] * dp[i - 1][0]) % mod + (dp[0][1] * dp[i - 1][2]) % mod + (dp[0][2] * dp[i - 1][1]) % mod) % mod
    dp[i][1] = ((dp[0][0] * dp[i - 1][1]) % mod + (dp[0][1] * dp[i - 1][0]) % mod + (dp[0][2] * dp[i - 1][2]) % mod) % mod
    dp[i][2] = ((dp[0][1] * dp[i - 1][1]) % mod + (dp[0][0] * dp[i - 1][2]) % mod + (dp[0][2] * dp[i - 1][0]) % mod) % mod
print(dp[-1][0])
