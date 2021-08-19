# 96 C - Typical Stairs
N, M = map(int, input().split())
A = [int(input()) for _ in range(M)]
A = set(A)
MOD = 1000000007

dp = [0] * (N + 1)
dp[0] = 1
for i in range(1, N + 1):
    if i in A:
        continue
    dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
print(dp[N])
