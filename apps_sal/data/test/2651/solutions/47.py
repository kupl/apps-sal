N,M = map(int,input().split())
X = list(map(int,input().split()))
Y = list(map(int,input().split()))
a = 0
b = 0
mod = 10**9+7

for n in range(N):
  a+=(2*n-N+1)*X[n]
  a%=mod

for m in range(M):
  b+=(2*m-M+1)*Y[m]
  b%=mod

print(a*b%mod)
