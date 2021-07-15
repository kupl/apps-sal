N, M = map(int, input().split())
# 0段目からN段目まで、壊れているか否かを表す flag
issafe = [1] * (N+1)
for i in range(M):
  a = int(input())
  issafe[a] = 0

mod = 10**9 + 7

# 0段目からN段目までの移動方法の数
dp = [0] * (N + 1)
dp[0] = 1
if issafe[1]: dp[1] = 1
# 漸化式に従って計算する
for i in range(2, N + 1):
  if issafe[i-1]: dp[i] += dp[i-1]
  if issafe[i-2]: dp[i] += dp[i-2]
  dp[i] %= mod
  
print(dp[N])
