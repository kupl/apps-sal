N,K = map(int,input().split())
a = 0
for i in range(K,N+2):
  a += 1 + (N+1-i)*i
print(a%(10**9+7))
