l, r = map(int, input().split())
M = len(bin(r)) - 2
L = format(l, "b").zfill(M)
R = format(r, "b")
mod = 10**9 + 7
dp = [[0 for l in range(70)] for i in range(5)]
if L[0] == "1":
    dp[2][0] = 1
else:
    dp[3][0] = 1
    dp[0][0] = 1
for i in range(1, M):
    if L[i] == "1" and R[i] == "1":
        dp[1][i] = (dp[0][i - 1] + dp[1][i - 1]) % mod
        dp[2][i] = (dp[2][i - 1]) % mod
        dp[3][i] = (2 * dp[3][i - 1]) % mod
        dp[4][i] = (dp[3][i - 1] + 3 * dp[4][i - 1]) % mod
    elif L[i] == "1" and R[i] == "0":
        dp[1][i] = dp[1][i - 1] + dp[0][i - 1]
        dp[3][i] = dp[3][i - 1]
        dp[4][i] = (dp[4][i - 1] * 3) % mod
    elif L[i] == "0" and R[i] == "1":
        dp[0][i] = dp[0][i - 1]
        dp[1][i] = (2 * dp[1][i - 1] + dp[2][i - 1]) % mod
        dp[2][i] = dp[2][i - 1]
        dp[3][i] = (dp[2][i - 1] + dp[3][i - 1] * 2) % mod
        dp[4][i] = (dp[0][i - 1] + dp[1][i - 1] + dp[3][i - 1] + dp[4][i - 1] * 3) % mod
    else:
        dp[0][i] = dp[0][i - 1]
        dp[1][i] = (dp[1][i - 1] * 2) % mod
        dp[2][i] = dp[2][i - 1]
        dp[3][i] = (dp[3][i - 1]) % mod
        dp[4][i] = (dp[0][i - 1] + dp[1][i - 1] + dp[4][i - 1] * 3) % mod
ans = 0
for i in range(5):
    ans += dp[i][M - 1]
    ans %= mod
print(ans)
