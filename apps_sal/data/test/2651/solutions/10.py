n,m=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
mod=10**9+7
x.sort()
y.sort()
sx,sy=0,0
for k in range(1,n+1):
  sx+=(2*k-n-1)*x[k-1]
  sx%=mod
for k in range(1,m+1):
  sy+=(2*k-m-1)*y[k-1]
  sy%=mod
print((sx*sy)%mod)
