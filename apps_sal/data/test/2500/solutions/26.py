import os
import sys
if os.getenv('LOCAL'):
    sys.stdin = open('_in.txt', 'r')
sys.setrecursionlimit(2147483647)
INF = float('inf')
IINF = 10 ** 18
MOD = 10 ** 9 + 7
N = int(sys.stdin.readline())
dp = [[0] * 3 for _ in range(N.bit_length())]
dp[-1][1] = 1
dp[-1][0] = 1
for i in reversed(list(range(N.bit_length() - 1))):
    if N >> i & 1:
        dp[i][1] += dp[i + 1][0]
        dp[i][2] += dp[i + 1][1]
        dp[i][2] += dp[i + 1][2]
        dp[i][0] += dp[i + 1][0]
        dp[i][2] += dp[i + 1][1]
        dp[i][2] += dp[i + 1][2]
        dp[i][1] += dp[i + 1][1]
        dp[i][2] += dp[i + 1][2]
    else:
        dp[i][0] += dp[i + 1][0]
        dp[i][2] += dp[i + 1][1]
        dp[i][2] += dp[i + 1][2]
        dp[i][1] += dp[i + 1][1]
        dp[i][2] += dp[i + 1][2]
        dp[i][0] += dp[i + 1][1]
        dp[i][2] += dp[i + 1][2]
    dp[i][0] %= MOD
    dp[i][1] %= MOD
    dp[i][2] %= MOD
print(sum(dp[0]) % MOD)
