n,m=map(int,input().split())
lrd=[list(map(int,input().split())) for _ in range(m)]
g=[[] for _ in range(n)]
for l,r,d in lrd:
  g[l-1].append([d,r-1])
  g[r-1].append([-d,l-1])

no_seen=set(range(n))
inf=float('inf')
dst=[inf]*n
while no_seen:
  todo=[[0,no_seen.pop()]]
  #print(todo)
  while todo:
    d,t=todo.pop()
    no_seen.discard(t)
    l=g[t]
    for di,ti in l:
      if dst[ti]!=inf and dst[ti]!=d+di:
        print('No')
        return
      elif dst[ti]!=inf and dst[ti]==d+di:
        pass
      else:
        todo.append([d+di,ti])
        dst[ti]=d+di

print('Yes')
