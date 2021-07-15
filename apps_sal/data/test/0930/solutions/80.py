from sys import stdin
#入力
readline=stdin.readline
N,K=map(int,readline().split())

mod=10**9+7
fact=[1]*(2*N)
finv=[1]*(2*N)
inv=[1]*(2*N)
inv[0]=0
for i in range(2,2*N):
    fact[i]=(fact[i-1]*i%mod)
    inv[i]=(-inv[mod%i]*(mod//i))%mod
    finv[i]=(finv[i-1]*inv[i])%mod

def com(N,K,mod):
    if (K<0) or (N<K):
        return 0
    return fact[N]*finv[K]*finv[N-K]%mod

if N-1<=K:
    print(com(2*N-1,N,mod))

else:
    res=0
    for m in range(K+1):
        res+=com(N,m,mod)*com(N-1,m,mod)
        res%=mod
    print(res)
