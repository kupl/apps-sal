N,M,K=map(int,input().split())
mod = 998244353

factorial=[1 for i in range(N+1)]
for i in range(1,N+1):
    if i==1:factorial[i]=1
    else:factorial[i] = factorial[i-1]*i % mod

def comb(n,k):
    return (factorial[n]*pow(factorial[n-k]*factorial[k], -1, mod))%mod

def count(n,m,k):
  return m*comb(n-1,k)*pow(m-1,n-k-1,mod)%mod

print(sum([count(N,M,i) for i in range(K+1)]) % mod)
