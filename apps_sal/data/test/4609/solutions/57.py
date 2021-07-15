N=int(input())
d={}
for _ in range(N):
  a=int(input())
  if a in d:
    d[a]+=1
  else:
    d[a]=1
ans=0
for k,v in d.items():
  ans+=v%2
print(ans)
