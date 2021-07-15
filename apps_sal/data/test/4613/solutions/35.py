class UnionFind():
  def __init__(self,n):
    self.n = n
    self.parents = [-1]*n
  def find(self,x):
    if self.parents[x]<0:
      return x
    else:
      self.parents[x]=self.find(self.parents[x])
      return self.parents[x]
  def unite(self,x,y):
    x = self.find(x)
    y = self.find(y)
    if x == y:
      return
    if self.parents[x]>self.parents[y]:
      x,y=y,x
    self.parents[x]+=self.parents[y]
    self.parents[y]=x
  def same(self,x,y):
    return self.find(x)==self.find(y)
N,M = map(int,input().split())
A = [0]*M
t=0
B=[0]*M
for i in  range(M):
  a,b=map(int,input().split())
  A[i]=[a-1,b-1]
for t in range(M):
  UF = UnionFind(N)
  for i in range(M):
    if i!=t:
      UF.unite(A[i][0],A[i][1])
  if UF.same(A[t][0],A[t][1])==False:
    B[t]=1
print(sum(B))
