f=lambda:map(int,input().split())
n,st,sa=f()
g=[set() for _ in range(n)]
for _ in range(n-1):
  a,b=f()
  g[a-1].add(b-1)
  g[b-1].add(a-1)
def bfs(s):
  l=[-1]*n; l[s]=0; q=[s]
  while q:
    v=q.pop(); d=l[v]+1
    for c in g[v]:
      if l[c]<0: l[c]=d; q+=[c]
  return l
lt=bfs(st-1)
la=bfs(sa-1)
print(max(la[i] for i in range(n) if lt[i]<la[i])-1)
