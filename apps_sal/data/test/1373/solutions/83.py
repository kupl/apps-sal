N,K=map(int,input().split())
mod=10**9+7
s=0
for i in range(K,N+2):
  s+=(2*N-i+1)*i//2-i*(i-1)//2+1
print(s%mod)
