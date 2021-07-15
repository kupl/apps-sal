n,k = map(int,input().split())

ans=0
mod = 10**9+7
for i in range(k,n+2):
  a0=(i*(i-1))//2
  an=i*n-a0
  ans+=an-a0+1

print(ans%mod)
