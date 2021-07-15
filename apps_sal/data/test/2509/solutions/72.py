N,K = map(int,input().split())
ans = 0

for n in range(K+1,N+1):
  ans+=N//n*(n-K)+max(N%n-max(K-1,0),0)

print(ans)
