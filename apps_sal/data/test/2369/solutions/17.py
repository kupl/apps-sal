N,K=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
mod=10**9+7
f=[1]
for i in range(N):
  f+=[f[-1]*(i+1)%mod]
def comb(a,b):
  return f[a]*pow(f[b],mod-2,mod)*pow(f[a-b],mod-2,mod)%mod

    
max=0
for i in range(K-1,N):
  max+=comb(i,K-1)*A[i]
  max%=mod
for i in range(N-K+1):
  max-=comb(N-i-1,K-1)*A[i]
  max%=mod
print(max)
