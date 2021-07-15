r,D,x0=map(int,input().split())

ans=x0

for i in range(10):
  ans=r*ans-D
  print(ans)
