from collections import defaultdict
a=input().strip()
n=len(a)
g=defaultdict(list)
for i in range(n):
 g[a[i]].append(i)
vis={}
vis[0]=0
q=[0]
while len(q)!=0:
 tmp=q.pop(0)
 if tmp==n-1:
  break 
 val=a[tmp]
 s=len(g[val])
 for i in range(s):
  if g[val][i] not in vis:
   vis[g[val][i]]=vis[tmp]+1 
   q.append(g[val][i])
 g[val]=[]
 if tmp+1<=n-1 and tmp+1 not in vis:
  q.append(tmp+1)
  vis[tmp+1]=vis[tmp]+1 
 if tmp-1>=0 and tmp-1 not in vis:
  q.append(tmp-1)
  vis[tmp-1]=vis[tmp]+1
print(vis[n-1])
 
   

