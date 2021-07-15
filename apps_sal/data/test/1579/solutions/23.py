import sys
input = sys.stdin.readline
max_n = 10**5
ans = 0
n = int(input())

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.sizea = [1 if _ < n//2 else 0 for _ in range(n)]
        self.sizeb = [0 if _ < n//2 else 1 for _ in range(n)]
        self.sizec = [1 for _ in range(n)]
        self.rank = [0] * (n)
        
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def is_root(self, x):
        if self.par[x] == x:
            return True
        else:
            return False
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
            self.sizea[x] += self.sizea[y]
            self.sizeb[x] += self.sizeb[y]
            self.sizec[x] += self.sizec[y]
        else:
            self.sizec[x] += 1          

    def get_size(self, x):
        x = self.find(x)
        return self.sizea[x],self.sizeb[x],self.sizec[x]

uf = UnionFind(2*max_n)

for _ in range(n):
  x,y = map(int, input().split())
  x -= 1
  y += max_n - 1
  uf.union(x, y)

for i in range(max_n):
  if uf.is_root(i):
    a,b,c = uf.get_size(i)
    if a*b > 1:
      ans += a*b -(c-1)
print(ans)
