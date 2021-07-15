N=int(input())
c1=input()
c2=input()
c3=input()
c4=input()

mod=10**9+7
dp=[[0]*2 for _ in range(N)]
dp[0][0]=1
dp[0][1]=0
for i in range(1,N):
  dp[i][0]=(dp[i-1][0]+dp[i-1][1])%mod
  dp[i][1]=dp[i-1][0]
x=dp[N-1][1]

if N==2:
  print(1)
  return

if c2=="A":
  if c1=="A":
    print(1)
    return
  else:
    if c3=="A":
      print(x)
      return
    else:
      print(pow(2,N-3,mod))
      return
else:
  if c4=="B":
    print(1)
    return
  else:
    if c3=="B":
      print(x)
      return
    else:
      print(pow(2,N-3,mod))
      return
