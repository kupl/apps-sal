class UnionFind():
  def __init__(self, n):
    self.n=n
    self.parents=[-1]*n

  def find(self,x):
    if self.parents[x]<0:
      return x
    else:
      self.parents[x]=self.find(self.parents[x])
      return self.parents[x]

  def unite(self, x, y):
    x = self.find(x)
    y = self.find(y)
    if x == y:
      return
    if self.parents[x]>self.parents[y]:
      x,y=y,x
    self.parents[x]+=self.parents[y]
    self.parents[y]=x

  def size(self, x):
    return -self.parents[self.find(x)]

  def same(self, x, y):
    return self.find(x) == self.find(y)

  def roots(self):
    return [i for i,x in enumerate(self.parents) if x<0]

N,M=map(int,input().split())
uf=UnionFind(N)
for _ in range(M):
  a,b=map(int,input().split())
  uf.unite(a-1,b-1)
ans=0
for r in uf.roots():
  s=uf.size(r)
  ans=max(ans,s)
print(ans)
