import sys
sys.setrecursionlimit(10**9)
N,M=map(int,input().split())

graph=[set() for _ in range(N+1)]
for _ in range(M):
  A,B=map(int,input().split())
  graph[A].add(B)
#print(graph)

visited=[False]*(N+1)
def dfs(path):
  nonlocal cycle
  u=path[-1]
  
  visited[u]=True  
  for v in graph[u]:
    if visited[v]:
      cycle=list(path+[v])
      return
    else:
      dfs(path+[v])      
    if cycle:
      return    
  visited[u]=False
  
cycle=[]
for i in range(1,N+1):
  dfs([i])
  if cycle:
    break
else:
  print(-1)
  return
    
#remove prefix  
for i in range(len(cycle)):
  if cycle[i]==cycle[-1]:
    cycle=cycle[i:]
    break
#print(cycle)

cycle_set=set(cycle)
subgraph=[set() for _ in range(N+1)]
for c in cycle_set:
  for v in graph[c]:
    if v in cycle_set:
      subgraph[c].add(v)
#print(subgraph)    

#visited=[False]*(N+1)
ex_path=[]
def dfs2(path,t):
  nonlocal ex_path
  u=path[-1]
  if u==t:
    ex_path=path
    return
  
  for v in graph[u]:
    dfs2(path+[v],t)
    if ex_path:
      return

graph=subgraph
while True:
  for i in range(len(cycle)-1):
    u=cycle[i]
    v=cycle[i+1]
    w=-1
    if len(graph[u])>1:
      for x in graph[u]:
        if x!=v:
          w=x
          break
      break
  else:
    print(len(cycle)-1)
    for i in range(len(cycle)-1):
      print(cycle[i])
    return
    
  #print(u,v,w)
  #w->u
  dfs2([w],u)
  cycle=ex_path+[w]
  #print(cycle)
  cycle_set=set(cycle)
  subgraph=[set() for _ in range(N+1)]
  for c in cycle_set:
    for v in graph[c]:
      if v in cycle_set:
        subgraph[c].add(v)
        
  graph=subgraph
