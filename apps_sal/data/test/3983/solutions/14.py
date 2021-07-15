from collections import defaultdict

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

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
      
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]


def main():
  N, M  = list(map(int,input().split()))

  uf = UnionFind(N)
  edge_num = 0
  for _ in range(M):
    a, b = list(map(int,input().split()))
    a -= 1
    b -= 1
    uf.union(a, b)
    edge_num += 1
  edge_total = (N*(N-1)//2)

  if N % 2 == 1:
    if (edge_num + edge_total) % 2 == 1:
      print("First")
    else:
      print("Second")
    return


  p1 = uf.find(0)
  p2 = uf.find(N-1)
  s1 = uf.size(p1)

  odds = 0
  for i in range(N):
    if i != uf.find(i) or i == p1 or i == p2: continue
    if uf.size(i) % 2 == 1:
      odds += 1

  if odds % 2 == 1:
    print("First")
    return
  if (edge_total + edge_num + s1) % 2 == 1:
    print("First")
  else:
    print("Second")
  return

T = int(input())
for _ in range(T):
  main()



