from itertools import product
N,M=map(int,input().split())
x,y,z = [0]*N, [0]*N, [0]*N
for i in range(N):
  x[i],y[i],z[i] = map(int,input().split())

prod= product([1,-1],repeat=3)
ans=0
for p in prod:
  s=[(p[0]*x[i]+p[1]*y[i]+p[2]*z[i]) for i in range(N)]
  s.sort(reverse=True)
  tmp=sum(s[:M])
  ans=max(ans,tmp)
print(ans)
