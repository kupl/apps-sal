n=int(input())
c=sorted(list(map(int,input().split())),reverse=True)
ans=0
mod=10**9+7
for i in range(1,n+1):
  ans+=c[i-1]*(i+1)%mod
print(4**(n-1)*ans%mod)
