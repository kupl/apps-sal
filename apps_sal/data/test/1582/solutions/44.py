N=int(input())
dp=[[0]*10 for _ in range(10)]
for i in range(1,N+1):
  a=str(i)
  dp[int(a[0])][int(a[-1])]+=1
ans=0
for i in range(10):
  for j in range(10):
    ans+=dp[i][j]*dp[j][i]
print(ans)
