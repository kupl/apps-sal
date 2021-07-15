class UnionFind(object):
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
            self.size[x] += self.size[y] 

    def is_same(self, x, y):
        return self.find(x) == self.find(y)
      
    def get_size(self, x):
        x = self.find(x)
        return self.size[x]

n,m,k=map(int,input().split())
uf=UnionFind(n+1)
cnt=[0]*(n+1)
for _ in range(m):
  a,b=map(int,input().split())
  uf.union(a,b)
  cnt[a]+=1
  cnt[b]+=1
for _ in range(k):
  c,d=map(int,input().split())
  if uf.is_same(c,d):
    cnt[c]+=1
    cnt[d]+=1
for i in range(1,n+1):
  print(uf.get_size(i)-cnt[i]-1,end=' ')
