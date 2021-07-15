n,m=map(int,input().split())
ks=[[] for i in range(m)]
for i in range(m):
  ks[i]=list(map(lambda x:int(x)-1,input().split()))
p=list(map(int,input().split()))

ans=0
for i in range(1<<n):
  l=[0]*n
  for j in range(n):
    l[j]=1 if i&1 else 0
    i>>=1
  
  # light check
  for j in range(m):
    s=sum([l[k] for k in ks[j][1:]])
    if s%2!=p[j]:
      break
  else:
    ans+=1

print(ans) 
