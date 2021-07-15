from collections import deque

n=int(input())
ch=0
g=[[] for _ in range(n)]
k=[[] for _ in range(n)]
for i in range(n-1):
  u,v,w=list(map(int,input().split()))
  if w%2==0:
    g[u-1].append(v-1)
    g[v-1].append(u-1)
  else:
    k[u-1].append(v-1)
    k[v-1].append(u-1)
    ch1=u-1
    ch2=v-1
    ch=1

## 0:White 1:Black
ans=[-1 for _ in range(n)]

if ch>0:
  ans[ch1]=0
  d=[ch1]
  qu=deque(d)
  while qu:
    p=qu.popleft()
    
    for gr in g[p]:
      if ans[gr]==-1:
        if ans[p]==0:
          ans[gr]=0
          qu.append(gr)
        else:
          ans[gr]=1
          qu.append(gr)
      
    for kr in k[p]:
      if ans[kr]==-1:
        if ans[p]==0:
          ans[kr]=1
          qu.append(kr)
        else:
          ans[kr]=0
          qu.append(kr)   
    
          
  for j in range(n):
    print((ans[j]))
    
else:
  for j in range(n):
    print((0))
      
  


