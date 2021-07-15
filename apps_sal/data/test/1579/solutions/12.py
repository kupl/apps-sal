N = int(input())
XY = [tuple(map(int,input().split())) for i in range(N)]

class UnionFind:
    def __init__(self,N):
        self.parent = [i for i in range(N)]
        self._size = [1] * N
        self.count = 0
    def root(self,a):
        if self.parent[a] == a:
            return a
        else:
            self.parent[a] = self.root(self.parent[a])
            return self.parent[a]
    def is_same(self,a,b):
        return self.root(a) == self.root(b)
    def unite(self,a,b):
        ra = self.root(a)
        rb = self.root(b)
        if ra == rb: return
        if self._size[ra] < self._size[rb]: ra,rb = rb,ra
        self._size[ra] += self._size[rb]
        self.parent[rb] = ra
        self.count += 1
    def size(self,a):
        return self._size[self.root(a)]

M = 10**5
uf = UnionFind(2*M)
for x,y in XY:
    a,b = x-1,y-1+M
    if uf.is_same(a,b): continue
    uf.unite(a,b)
for i in range(2*M):
    uf.root(i)

rt = []
for i in range(2*M):
    rt.append(uf.root(i))
from collections import Counter
xr = Counter(rt[:M])
yr = Counter(rt[M:])

ans = 0
for k,v in xr.items():
    ans += yr[k] * v
ans -= N
print(ans)
