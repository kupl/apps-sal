n,a,b=map(int,input().split())
mod=10**9+7
ans=pow(2,n,mod)-1
a=min(a,n-a)
b=min(b,n-b)
c=min(a,b)
wk=1
for i in range(1,c+1):
  wk=wk*(n+1-i)*pow(i,mod-2,mod)%mod
ans-=wk
for i in range(c+1,max(a,b)+1):
  wk=wk*(n+1-i)*pow(i,mod-2,mod)%mod
ans-=wk
print(ans%mod)
