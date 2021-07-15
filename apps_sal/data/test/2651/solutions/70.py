N,M=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
mod=10**9+7

X=0
for i in range(N):
    X+=((i)*x[i]-(N-i-1)*x[i])
    X%=mod
Y=0
for i in range(M):
    Y+=((i)*y[i]-(M-i-1)*y[i])
    Y%=mod
print(X*Y%mod)
