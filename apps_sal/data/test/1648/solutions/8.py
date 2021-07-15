N,K=map(int,input().split())
mod=10**9+7

factorial=[1 for i in range(N+1)]
for i in range(1,N+1):
    if i==1:factorial[i]=1
    else:factorial[i] = factorial[i-1]*i % mod

def comb(n,k):
    return factorial[n]*pow(factorial[n-k]*factorial[k], -1, mod)

for i in range(1,K+1):
  if i > N-K+1:print(0)
  else:print(comb(K-1,i-1)*comb(N-K+1,i)%mod)
