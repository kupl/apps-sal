N, M = map(int, input().split())
 
# issafe => 0段目からN段目まで, 安全ならTrue, 壊れているならFalse
issafe = [1] * (N+1)
for i in range(M):
  a = int(input())
  issafe[a] = 0

# 動的計画法（漸化式）
# dp => 0段目からN段目まで, その移動方法の数
dp = [0] * (N+1)
dp[0] = 1
if issafe[1]: dp[1] = 1
for i in range(2, N+1):
  if issafe[i-1]: dp[i] += dp[i-1]
  if issafe[i-2]: dp[i] += dp[i-2]
  dp[i] %= 10**9+7
    
print(dp[N])
