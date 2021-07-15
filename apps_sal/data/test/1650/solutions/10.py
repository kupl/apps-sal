L=input()
N=len(L)
dp=[[0,0]for _ in range(N)]
dp[0][0]=1 #以下が確定（0）
dp[0][1]=2 #以下が確定してない（1,0）と逆
mod=10**9+7
for i in range(1,N):
  #以下モードは3倍に配給パターンが増える
  dp[i][0]+=3*dp[i-1][0]
  dp[i][0]%=mod
  if L[i]=='0':
    #(0,0)を配給し、そのまま
    dp[i][1]+=dp[i-1][1]
  else:
    #(0,0)を配給すれば、以下モードに移る
    dp[i][0]+=dp[i-1][1]
    #(1,0)(0,1)を配給する
    dp[i][1]+=dp[i-1][1]*2
  dp[i][0]%=mod
  dp[i][1]%=mod
print(sum(dp[-1])%mod)
