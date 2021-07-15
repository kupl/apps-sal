def nCk(_n,_k):
  return fact[_n]*pow(fact[_k],m-2,m)*pow(fact[_n-_k],m-2,m)%m

fact=[1]*2005
for i in range(1,2004):
  fact[i]=fact[i-1]*i

n,k=list(map(int,input().split()))
m=10**9+7

for i in range(1,k+1):
  print((nCk(n-k+1,i)*nCk(k-1,i-1)%m if n-k>=i-1 else 0))

