from math import factorial
MOD = 10 ** 9 + 7
k = int(input())
bink = list(map(int, bin(k)[2:]))
N = len(bink)
dp = [[[0, 0] for j in range(i + 2)] for i in range(N + 1)]
dp[0][0][1] = 1
for i in range(1, N + 1):
    for j in range(i + 1):
        dp[i][j][0] += 2 ** j * dp[i - 1][j][0]
        if j:
            dp[i][j][0] += dp[i - 1][j - 1][0]
        odd = 2 ** (j - 1) if j else 0
        even = 2 ** j - odd
        if bink[i - 1] == 1:
            dp[i][j][0] += even * dp[i - 1][j][1]
        if bink[i - 1] == 0:
            dp[i][j][1] += even * dp[i - 1][j][1]
        else:
            dp[i][j][1] += odd * dp[i - 1][j][1]
            if j:
                dp[i][j][1] += dp[i - 1][j - 1][1]
ans = sum(map(sum, dp[-1]))
print(ans % MOD)
