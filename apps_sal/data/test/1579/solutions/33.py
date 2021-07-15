n=int(input())
xy=[list(map(int,input().split())) for _ in range(n)]
maxx=max([x for x,y in xy])
maxy=max([y for x,y in xy])
g=[[] for _ in range(maxx+maxy+1)]
for x,y in xy:
  y+=maxx
  g[x].append(y)
  g[y].append(x)
# 1より大きい奇数回で到達可能な頂点にパスを追加していく。最短距離が3以上の奇数の頂点のペアの数。奇数のパスを数え、最後にパスの数を引く
mi=set(range(maxx+maxy+1))
ans=0
while mi:
  v=mi.pop()
  todo=[v]
  nx=0
  ny=0
  while todo:
    v=todo.pop()
    if v<=maxx:
      nx+=1
    else:
      ny+=1
    for nv in g[v]:
      if nv in mi:
        mi.discard(nv)
        todo.append(nv)
  ans+=nx*ny
print((ans-n))

