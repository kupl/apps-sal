MOD = 10**9 + 7
N, M = map(int, input().split())
dp = [0]*(N+1)
for _ in range(M):
  dp[int(input())] = -1
dp[0] = 1

for i in range(N+1):
  if dp[i] == -1:
    continue
  if i+1 <= N and dp[i+1] != -1:
    dp[i+1] = (dp[i+1] + dp[i]) % MOD
  if i+2 <= N and dp[i+2] != -1:
    dp[i+2] = (dp[i+2] + dp[i]) % MOD
print(dp[N])
