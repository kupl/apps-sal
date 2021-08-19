import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
MOD = 10 ** 9 + 7
N = readline().decode().rstrip()
L = len(N)
dp = [[0] * 2 for _ in range(L + 1)]
dp[0][0] = 1
for i in range(L):
    nd = int(N[i])
    if nd == 0:
        dp[i + 1][0] = dp[i][0]
        dp[i + 1][1] = 3 * dp[i][1] % MOD
    else:
        dp[i + 1][0] = 2 * dp[i][0] % MOD
        dp[i + 1][1] = (3 * dp[i][1] + dp[i][0]) % MOD
print(sum(dp[L]) % MOD)
