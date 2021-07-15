import sys
input = lambda:sys.stdin.readline().rstrip()
sys.setrecursionlimit(300000)

class UnionFind:
  def __init__(self, n):
    self.n = [-1]*n
    self.r = [0]*n
    self.siz = n

  def find_root(self, x):
    if self.n[x] < 0:
      return x
    else:
      self.n[x] = self.find_root(self.n[x])
      return self.n[x]

  def unite(self, x, y):
    x = self.find_root(x)
    y = self.find_root(y)
    if x == y:
      return
    elif self.r[x] > self.r[y]:
      self.n[x] += self.n[y]
      self.n[y] = x
    else:
      self.n[y] += self.n[x]
      self.n[x] = y
      if self.r[x] == self.r[y]:
        self.r[y] += 1
    self.siz -= 1

  def root_same(self, x, y):
    return self.find_root(x) == self.find_root(y)

  def count(self, x):
    return -self.n[self.find_root(x)]

  def size(self):
    return self.siz

"""
N
頂点数のペア -> 追加できる辺の数
7
1 6 -> 0 + 15 -> 15
2 5 -> 1 + 10 -> 11
3 4 -> 3 + 6  -> 9

8
1 7 -> 0 + 21 -> 21
2 6 -> 1 + 15 -> 16
3 5 -> 3 + 10 -> 13
4 4 -> 6 + 6 -> 12
"""
F="First"
S="Second"
for _ in range(int(input())):
  n,m=map(int,input().split())
  uf=UnionFind(n)
  for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    uf.unite(a,b)
  if n%2==1:
    if (n*(n-1)//2-m)%2==1:
      print(F)
    else:
      print(S)
    continue
  s=uf.count(0)
  e=uf.count(n-1)
  if (n*(n-1)//2-s*e-m)%2==1 or s%2!=e%2:
    print(F)
  else:
    print(S)
