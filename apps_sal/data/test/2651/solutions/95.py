MOD=10**9+7
n,m=map(int,input().split())
xs=list(map(int,input().split()))
ys=list(map(int,input().split()))
x=0
for i in range(n):
  x+=(2*(i+1)-n-1)*xs[i]
  x%=MOD

y=0
for j in range(m):
  y+=(2*(j+1)-m-1)*ys[j]
  y%=MOD

print(x*y%MOD)
