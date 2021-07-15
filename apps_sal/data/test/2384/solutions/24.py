N=int(input())
A=list(map(int, input().split()))
if N==2:
  print(max(A))
  return 
  
dp=[[0,0,0] for i in range(N)]
dp[0][0]=A[0]
dp[1][1]=A[1]
dp[2][2]=A[2]
for i in range(N):
  if i>1:
    dp[i][0]=dp[i-2][0]+A[i]
  if i>2:
    dp[i][1]=max(dp[i-3][0],dp[i-2][1])+A[i]
  if i>3 :
    dp[i][2]=max(dp[i-4][0],dp[i-3][1],dp[i-2][2])+A[i]
if N%2==1:
  ans=max(dp[-1][2],dp[-2][1],dp[-3][0])
else:
  ans=max(dp[-1][1],dp[-2][0])
print(ans)
