class Node:
  def __init__(self, v):
    self.v = v
    self.p = None
    self.n = None
  
  def delete(self):
    if self.p:
      self.p.n = self.n
    if self.n:
      self.n.p = self.p

N = int(input())
pp = list(map(int, input().split()))
nn = dict()
prev = None
for i, p in enumerate(pp):
  n = Node(i)
  if prev:
    prev.n = n
    n.p = prev
  nn[p] = n
  prev = n
s = 0
for x in range(1, N):
  c = nn[x]
  ci = c.v
  pi = c.p.v if c.p else -1
  ni = c.n.v if c.n else N
  if c.p:
    ppi = c.p.p.v if c.p.p else -1
    s += x * (pi - ppi) * (ni - ci)
  if c.n:
    nni = c.n.n.v if c.n.n else N
    s += x * (ci - pi) * (nni - ni)
  c.delete()
print(s)
