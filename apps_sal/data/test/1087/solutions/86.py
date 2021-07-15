N,K=list(map(int,input().split()))
A=list(map(int, input().split()))
dp=[[0,0]for _ in range(42)]
#2の41乗が10**12とちょっと

for i in range(1,42):
  if dp[i-1][1]==1:
    dp[i][1]=1
  
  cnt=0
  #リストA内のiケタ目の1の数をカウント
  for j in range(N):
    if (A[j]>>(41-i))&1==1:
      cnt+=1
      
  #1の方が多いときは、0を当てはめる
  if cnt>=N-cnt:
    dp[i][0]=dp[i-1][0]+(2**(41-i))*cnt
    if (K>>(41-i))&1==1:
      dp[i][1]=1
  else:
    if dp[i][1]==1:
      dp[i][0]=dp[i-1][0]+(2**(41-i))*(N-cnt)
    else:
      if (K>>(41-i))&1==1:
        #そのケタが1ならば問題なし
        dp[i][0]=dp[i-1][0]+(2**(41-i))*(N-cnt)
      else:
        #桁が0ならば0にするしかない
        dp[i][0]=dp[i-1][0]+(2**(41-i))*cnt
print((dp[41][0]))

