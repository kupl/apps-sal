# python 3.4.3
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# library
# -------------------------------------------------------------
def init_fact(n,mod):
    fact,finv,inv = [1]*n,[1]*n,[1]*n
    for i in range(2,n):
        fact[i] = (fact[i-1]*i) % mod
        inv[i]  = mod - inv[mod%i] * (mod//i)%mod
        finv[i] = finv[i-1] * inv[i] % mod
    return (fact,finv,inv)
 
def nCr(n,r,mod,fact,finv):
    if n<r:
        return 0
    else:
        return fact[n] * (finv[r] * finv[n-r] % mod) % mod

mod = 10**9+7
fact,finv,inv = init_fact(200010,mod)


# -------------------------------------------------------------
# main
# -------------------------------------------------------------

N,M,K = map(int,input().split())

ans = 0
for d in range(1,N):
    t = d * nCr(N*M-2, K-2, mod, fact, finv)
    t %= mod
    t *= (N-d)*M*M
    t %= mod
    ans += t
    ans %= mod
for d in range(1,M):
    t = d * nCr(N*M-2, K-2, mod, fact, finv)
    t %= mod
    t *= (M-d)*N*N
    t %= mod
    ans += t
    ans %= mod

print(ans)
