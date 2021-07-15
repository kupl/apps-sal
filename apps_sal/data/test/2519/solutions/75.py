N, K = map(int, input().split())
p=list(map(int,input().split()))

for i in range(N):
  p[i]=(1+p[i])/2
  
ans=[0]*(N-K+1)
ans[0]=sum(p[:K])
for i in range(1, N-K+1):
  ans[i]=ans[i-1]-p[i-1]+p[i+K-1]

print(max(ans))
