from collections import deque


def main():
  n,q=map(int,input().split())
  node=[[]*n for i in range(n)]
  for i in range(n-1):
    a,b=map(lambda x:int(x)-1,input().split())
    node[b].append(a)
    node[a].append(b)
  
  ans=[0]*n
  for i in range(q):
    p,x=map(int,input().split())
    p-=1
    ans[p]+=x

  root=[0]*n
  edge=[[]*n for i in range(n)]
  root[0]=0
  q=deque([0])
  visited=[False]*n
  visited[0]=True
  
  while q:
    r=q.popleft()
    for e in node[r]:
      if not visited[e]:
        visited[e]=True
        q.append(e)
        root[e]=r
        edge[r].append(e)
  
  
  p=[0]*n
  q=deque(edge[0])
  visited=[False]*n
  while q:
    e=q.popleft()
    p[e]=p[root[e]]+1
    for e2 in edge[e]:
      if not visited[e2]:
        visited[e2]=True
        q.append(e2)
  
  p=sorted(enumerate(p), key=lambda x:x[1])
  for i in range(1,n):
    e=p[i][0]
    r=root[e]
    ans[e]+=ans[r]
    
  print(*ans,sep=' ')


def __starting_point():
  main()
__starting_point()
