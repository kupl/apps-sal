p = 10**9 + 7

N, M = map(int, input().split())
status = [1] * (N + 1)
for i in range(M):
    status[int(input())] = 0

dp = [0] * (N + 1)
dp[0] = 1

for i in range(N):
    if i + 1 <= N and status[i + 1]:
        dp[i + 1] += dp[i] % p
    if i + 2 <= N and status[i + 2]:
        dp[i + 2] += dp[i] % p

print(dp[N] % p)
