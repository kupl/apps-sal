N = input()
K = int(input())
L = len(N)

dp =[[[ 0 for _ in range(2)] for _ in range(5)] for _ in range(len(N)+1)]
# dp[i][j][flg] i+1桁目までで0以外の個数がj個
# flg = 1 -> N 以下が確定している

dp[0][1][1] = int(N[0])-1
dp[0][1][0] = 1
dp[0][0][1]=1
for i in range(1,L):
  for j in range(4):
    b = i-1 # hitotumae
    now = int(N[i])
    ## N上限に張り付いてる方
    if now == 0:
      dp[i][j][0] += dp[b][j][0]
    else:
      dp[i][j][1] += dp[b][j][0]
      dp[i][j+1][1] += dp[b][j][0] * (now-1)
      dp[i][j+1][0] += dp[b][j][0]
    ## 張り付いてない方
    dp[i][j][1] += dp[b][j][1]
    dp[i][j+1][1] += dp[b][j][1] * 9
  

print((dp[L-1][K][0] + dp[L-1][K][1]))

