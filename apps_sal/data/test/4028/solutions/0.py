MOD=10**9+7
n=int(input())
s=[c=='(' for c in input()]
m=len(s)
z=[[0,0]]
for v in s:
 a=z[-1][v]
 z[-1][v]=len(z)
 z.append(z[a][:])
z[m][0]=z[m][1]=m
dp=[[0 for _ in range(m+1)] for _ in range(n+1)]
dp[0][0]=1
for _ in range(2*n):
 ndp=[[0 for _ in range(m+1)] for _ in range(n+1)]
 for i in range(n+1):
  for j in range(m+1):
   if dp[i][j]<1:continue
   if i>0:ndp[i-1][z[j][0]]=(ndp[i-1][z[j][0]]+dp[i][j])%MOD
   if i<n:ndp[i+1][z[j][1]]=(ndp[i+1][z[j][1]]+dp[i][j])%MOD
 dp=ndp
print(dp[0][m])
