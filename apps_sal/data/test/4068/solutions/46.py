N,M = map(int, input().split())
A = [int(input()) for _ in range(M)]

mod = 10**9 + 7

dp = [1] * (N+1)

for i in A:
    dp[i] = 0

for i in range(2, N+1):
        dp[i] *= (dp[i-1] + dp[i-2]) % mod

print(dp[-1])
