class UnionFind:
  '''
  UnionFind(n) : n頂点0辺の無向グラフを構築する O(n)
    p:親ノード番号(代表元以外)、木のサイズの負数(代表元)を格納
  leader(a)    : aの属する代表元を返す O(α(n))
  merge(a,b)   : a,bを辺で結び、代表元を返す O(α(n))
  same(a,b)    : a,bが連結か否かを返す O(α(n))
  size(a)      : aの属する連結成分のサイズを返す O(α(n))
  count()      : グループ数を返す O(n)
  groups()     : グラフをsetにグループ分けして返す O(n)
  '''
  def __init__(self, n):
    self.n = n
    self.p = [-1]*n
  def leader(self, a):
    while self.p[a]>=0:
      a = self.p[a]
    return a
  def merge(self, a, b):
    x = self.leader(a)
    y = self.leader(b)
    if x==y:
      return x
    if self.p[x]>self.p[y]:
      x, y = y, x
    self.p[x] += self.p[y]
    self.p[y] = x
    return x
  def same(self, a, b):
    return self.leader(a)==self.leader(b)
  def size(self, a):
    return -self.p[self.leader(a)]
  def count(self):
    return sum(i<0 for i in self.p)
  def groups(self):
    leader_buf = [0]*self.n
    group_size = [0]*self.n
    res = [set() for _ in range(self.n)]
    for i in range(self.n):
      leader_buf[i] = self.leader(i)
      group_size[leader_buf[i]] += 1
    for i in range(self.n):
      res[leader_buf[i]].add(i)
    res = [s for s in res if s]
    return res

f=lambda:map(int,input().split())
n,k=f()
A=[[*f()] for _ in range(n)]
ufh,ufw=UnionFind(n),UnionFind(n)
for y in range(n):
  for x in range(y):
    if all(A[h][x]+A[h][y]<=k for h in range(n)):
      ufw.merge(x,y)
    if all(A[x][w]+A[y][w]<=k for w in range(n)):
      ufh.merge(x,y)
M=998244353
F=[1]
for i in range(1,51): F+=[i*F[-1]%M]
c=1
for i in range(n):
  if ufh.p[i]<0: c=c*F[-ufh.p[i]]%M
  if ufw.p[i]<0: c=c*F[-ufw.p[i]]%M
print(c)
