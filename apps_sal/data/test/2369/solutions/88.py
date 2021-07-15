N,K=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
MOD=10**9+7
fan=[1]*(N+1)
for i in range(2,N+1):
    fan[i]=fan[i-1]*(i)%MOD
ans=0
def comb(a,b):
    return fan[a]*pow(fan[b],MOD-2,MOD)*pow(fan[a-b],MOD-2,MOD)%MOD
for i in range(N-K+1):
    ans=ans+comb(N-i-1,K-1)*(A[N-1-i]-A[i])
    ans%=MOD
print(ans)
