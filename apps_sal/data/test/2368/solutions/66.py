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
 
    def members(self, x): # 遅い
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
 
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
 
    def group_count(self):
        return len(self.roots())
 
    def all_group_members(self): # 遅い
        return {r: self.members(r) for r in self.roots()}
 
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
 
n,m=map(int,input().split())
 
uf = UnionFind(n)
 
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(m):
    c,d=map(int,input().split())
    c-=1
    d-=1
    uf.union(c,d)
weights_a = [0] * n
weights_b = [0] * n
for i in range(n):
    weights_a[uf.find(i)] += a[i]
    weights_b[uf.find(i)] += b[i]
for i in range(n):
    if weights_a[i] != weights_b[i]:
        print('No')
        return
print('Yes')
