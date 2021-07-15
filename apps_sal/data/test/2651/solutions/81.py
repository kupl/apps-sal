n,m=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
sumx,sumy=0,0
mod=10**9+7
for i in range(n):
    sumx+=i*x[i]-(n-i-1)*x[i]
sumx%=mod
for i in range(m):
    sumy+=i*y[i]-(m-i-1)*y[i]
sumy%=mod
print(sumx*sumy%mod)
