class UnionFind():
  def __init__(self, n, A, B):
    self.n = n
    self.parents = [-1] * n
    self.values = [a-b for a,b in zip(A,B)]

  def find(self, x):
    if self.parents[x] < 0:
      return x
    else:
      self.parents[x] = self.find(self.parents[x])
    return self.parents[x]

  def union(self, x, y):
    x = self.find(x)
    y = self.find(y)

    if x == y:
      return

    if self.parents[x] > self.parents[y]:
      x, y = y, x

    self.parents[x] += self.parents[y]
    self.values[x] += self.values[y]
    self.parents[y] = x

  def same(self, x, y):
    return self.find(x) == self.find(y)

  def roots(self):
    return [i for i, x in enumerate(self.parents) if x < 0]

  def members(self, x):
    root = self.find(x)
    return [i for i in range(self.n) if self.find(i) == root]

  def num_members(self,x):
    return abs(self.parents[self.find(x)])
  
  def groups(self):
    roots = self.roots()
    r_to_g = {}
    for i, r in enumerate(roots):
      r_to_g[r] = i
    groups = [[] for _ in roots]
    for i in range(self.n):
      groups[r_to_g[self.find(i)]].append(i)
    return groups

import sys,os,io
input = sys.stdin.readline
#input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
uf = UnionFind(N, A, B)
for i in range(M):
  c, d = list(map(int, input().split()))
  uf.union(c-1,d-1)
for i in range(N):
  if uf.parents[i]<0 and uf.values[i]!=0:
    print('No')
    return
print('Yes')


