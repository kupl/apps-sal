n,k=map(int,input().split())
mod=10**9+7
ans=[0]*(k+1)
anss=0
for i in range(k,0,-1):
  m=pow(k//i,n,mod)
  for j in range(i*2,k+1,i):m-=ans[j]
  ans[i]=m%mod
  anss+=ans[i]*i
  anss%=mod
print(anss)
