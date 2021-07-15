
#https://www.codechef.com/problems/DIGJUMP
 
import sys
import math
from collections import defaultdict
 
try: 
 sys.stdin = open('input.txt', 'r') 
 sys.stdout = open('output.txt', 'w')
 
except: 
 pass
 


 
 
s = input().strip()
at={}
n=len(s)
at=defaultdict(list)
for i in range(n):
 at[int(s[i])].append(i)

visited=defaultdict(lambda:False)
dist=defaultdict(lambda:float("inf"))
visited[0]=True
dist[0]=0
queue=[0]
added={}
while queue:
 u=queue.pop(0)
 char=int(s[u])
 for v in at[char]:
  if(not visited[v]):
   visited[v]=True
   queue.append(v)
   dist[v]=dist[u]+1

 at[char]=[]
 if(u!=0):
  v=u-1
  if(not visited[v]):
   visited[v]=True
   queue.append(v)
   dist[v]=dist[u]+1
 if(u!=n-1):
  v=u+1
  if(not visited[v]):
   visited[v]=True
   queue.append(v)
   dist[v]=dist[u]+1

print(dist[n-1])


