N,K=map(int,input().split())
A=list(map(int,input().split()))
mod = 10**9+7

if K==1:print(0)
else:
  factorial=[1 for i in range(N+1)]
  for i in range(1,N+1):
    if i==1:factorial[i]=1
    else:factorial[i] = factorial[i-1]*i % mod
  
  def comb(n,k):
    return factorial[n]*pow(factorial[n-k]*factorial[k], -1, mod)

  A1=sorted(A)
  A2=A1[::-1]
  
  ans=0
  for i in range(N-K+1):
    ans += (A2[i]-A1[i])*comb(N-i-1,K-1)
  ans %= mod

  print(ans)
