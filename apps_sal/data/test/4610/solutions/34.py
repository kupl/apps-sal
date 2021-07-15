n,k=list(map(int,input().split()))
a=list(map(int,input().split()))

d={}

for x in range(n):
  if a[x] not in d:
    d[a[x]]=0
  d[a[x]]+=1
  
ans=0
ans1=[]
for g in d:
  ans1.append(d[g])
  
if len(ans1)<=k:
  print((0))
  
else:
  ans1.sort()
  r=len(ans1)-k
  for t in range(r):
    ans+=ans1[t]
    
  print(ans)
  

