import sys

def BFS(K,edges,N):
  roots=[ [] for i in range(N)]
  for a,b,c in edges:
    roots[a]+=[(b,c)]
    roots[b]+=[(a,c)]
  dist=[-1]*N
  stack=[]
  stack.append(K)
  dist[K]=0
  while stack:
    label=stack.pop(-1)
    for i,c in roots[label]:
      if dist[i]==-1:
        dist[i]=dist[label]+c
        stack.append(i)
  return dist
      
      
a = []
edge = []
for l in sys.stdin:
    a.append(l.split())
V = int(a[0][0])
for i in range(V-1):
  buf = [int(a[i+1][0])-1, int(a[i+1][1])-1, int(a[i+1][2])]
  edge.append(buf)
n = int(a[V][0])
s = int(a[V][1])-1
ques = []
for i in range(n):
  buf = [int(a[V+i+1][0])-1, int(a[V+i+1][1])-1]
  ques.append(buf)
dist = BFS(s, edge, V)
for a, b in ques:
  res = dist[a] + dist[b]
  print(res)
