#abc135d
s=input()
mod=10**9+7
res=[0]*13
res[0]=1
for i in s:
 dp=[0]*13
 for j in range(13):
  dp[(j*10)%13]=res[j]%mod
 dp+=dp
 if i=='?':
  for k in range(13):
   res[k]=sum(dp[k+4:k+14])
 else:
  for k in range(13):
   res[k]=dp[k+13-int(i)]
print(res[5]%mod)

