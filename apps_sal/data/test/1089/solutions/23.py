N,M,K=map(int,input().split())
def cmb(x,y):
  X=1
  Y=1
  for i in range(1,y+1):
    X= X*(x+1-i)%MOD
    Y= Y*i%MOD
  return (X*pow(Y,MOD-2,MOD))%MOD
MOD=10**9+7
A=cmb(M*N-2, K-2)
ans=0
for d in range(1,N):
  ans+=d*(N-d)*M*M*A%MOD
for d in range(1,M):
  ans+=d*(M-d)*N*N*A%MOD
print(ans%MOD)
