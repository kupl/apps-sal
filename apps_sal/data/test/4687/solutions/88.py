N,K=map(int,input().split())
d={}
for i in range(N):
  a,b=map(int,input().split())
  if a not in d:
    d[a]=b
  else:
    d[a]+=b
d=sorted(d.items())
for i in d:
  K-=i[1]
  if K<=0:
    print(i[0])
    break
