n = int(input())
mod = 10**9+7
A=[1] + [0]*(n+3)
G=[1] + [0]*(n+3)
C=[1] + [0]*(n+3)
for i in range(1,n):
    t=(2*A[i-1]+G[i-1]+C[i-1])%mod
    A[i]=t
    G[i]=(t-A[i-2]+G[i-3])%mod
    C[i]=(t-A[i-2]-G[i-2]-3*A[i-3])%mod
print(((2*A[n-1]+G[n-1]+C[n-1])%mod))

