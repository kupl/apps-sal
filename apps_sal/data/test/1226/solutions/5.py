n,a,b=list(map(int,input().split()))
mod=10**9+7
factna=[n]
factnb=[n]
facta=[a]
factb=[b]
for i in range(1,a):
  factna.append(factna[-1]*(n-i)%mod)
  facta.append(facta[-1]*(a-i)%mod)
for i in range(1,b):
  factnb.append(factnb[-1]*(n-i)%mod)
  factb.append(factb[-1]*(b-i)%mod)
def pow(x,n):
  a=1
  while(n>0):
    if n%2==1:
      a*=x%mod
    x*=x%mod
    n>>=1
  return a
print(((pow(2,n)-1-factna[-1]*pow(facta[-1],mod-2)%mod-factnb[-1]*pow(factb[-1],mod-2)%mod)%mod))

