N = int(input())
mod = 10**9+7
A = [1]+(N+3)*[0]
G = [1]+(N+3)*[0]
C = [1]+(N+3)*[0]

for n in range(1,N):
  T = (2*A[n-1]+G[n-1]+C[n-1])%mod
  A[n] = T
  G[n] = (T-A[n-2]+G[n-3])%mod
  C[n] = (T-A[n-2]-G[n-2]-3*A[n-3])%mod

print((2*A[N-1]+G[N-1]+C[N-1])%mod)
