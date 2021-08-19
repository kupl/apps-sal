# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
N = int(input())

mod = 10**9 + 7
# bitも上から見ていくので逆順にして扱いやすくする
binN = format(N, "061b")[::-1]

dp = [[0, 0, 0] for _ in range(61)]
dp[60][0] = 1

for i in range(59, -1, -1):
    # i桁目のbitが 1
    if binN[i] == "1":
        dp[i][0] = dp[i + 1][0]
        dp[i][1] = dp[i + 1][0] + dp[i + 1][1]
        dp[i][2] = 2 * dp[i + 1][1] + 3 * dp[i + 1][2]
    # i桁目のbitが 0
    else:
        dp[i][0] = dp[i + 1][0] + dp[i + 1][1]
        dp[i][1] = dp[i + 1][1]
        dp[i][2] = dp[i + 1][1] + 3 * dp[i + 1][2]

    for j in range(3):
        dp[i][j] %= mod

print((dp[0][0] + dp[0][1] + dp[0][2]) % mod)
