# B - Values
# https://atcoder.jp/contests/arc106/tasks/arc106_b

class UnionFind():
  def __init__(self, n):
    self.n = n
    self.parents = [-1] * n
    
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
    self.parents[y] = x

  def size(self, x):
    return -self.parents[self.find(x)]

  def same(self, x, y):
    return self.find(x) == self.find(y)

  def members(self, x): # O(N)
    root = self.find(x)
    return [i for i in range(self.n) if self.find(i) == root]

  def all_group_members(self):
    self.group = {r:[] for r in self.roots()}
    for i in range(self.n):
      self.group[self.find(i)].append(i)
    return self.group

  def roots(self):
    return [i for i, x in enumerate(self.parents) if x < 0]

  def group_count(self):
    return len(self.roots())

  def __str__(self):
    return '\n'.join('{}: {}'.format(k, v) for k, v in list(self.all_group_members().items()))

n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
CD = [list(map(int, input().split())) for _ in range(m)] 

uf = UnionFind(n)
for c, d in CD:
  uf.union(c - 1, d - 1)

for key, val in list(uf.all_group_members().items()):
    if sum(A[i] for i in val) != sum(B[i] for i in val):
        print("No")
        return

print("Yes")


