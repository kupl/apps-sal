N,M = map(int,input().split())
LRD = [tuple(map(int,input().split())) for i in range(M)]

class WeightedUnionFind:
    def __init__(self,N):
        self.parent = [i for i in range(N)]
        self.rank = [0] * N
        self.count = 0
        self.weight = [0] * N
    def root(self,a):
        if self.parent[a] == a:
            return a
        else:
            pa = self.root(self.parent[a])
            self.weight[a] += self.weight[self.parent[a]]
            self.parent[a] = pa
            return pa
    def is_same(self,a,b):
        return self.root(a) == self.root(b)
    def unite(self,a,b,w):
        ra = self.root(a)
        rb = self.root(b)
        if ra == rb: return
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
            self.weight[ra] = w - self.weight[a] + self.weight[b]
        else:
            self.parent[rb] = ra
            self.weight[rb] = -w - self.weight[b] + self.weight[a]
            if self.rank[ra] == self.rank[rb]: self.rank[ra] += 1
        self.count += 1
    def diff(self,a,b):
        return self.weight[a] - self.weight[b]

uf = WeightedUnionFind(N)
for l,r,d in LRD:
    l,r = l-1,r-1
    if uf.is_same(l,r):
        if uf.diff(l,r) != d:
            print('No')
            return
    else:
        uf.unite(l,r,d)
print('Yes')
