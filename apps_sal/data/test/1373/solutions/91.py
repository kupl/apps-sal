N,K=map(int,input().split())
s=0
for i in range(K,N+2):
  s+=i*(N-i+1)+1
print(s%(10**9+7))
