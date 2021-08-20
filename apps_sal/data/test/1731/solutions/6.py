import sys
readline = sys.stdin.readline
MOD = 10 ** 9 + 7
(N, M) = map(int, readline().split())
dp = [0] + [1] * N
for _ in range(2 * M):
    dp2 = dp[:]
    for i in range(1, N + 1):
        dp2[i] = (dp2[i] + dp2[i - 1]) % MOD
    dp = dp2[:]
print(dp[N])
