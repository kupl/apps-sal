class UnionFind():
    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1] * n
    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            self.size[y] += self.size[x]
            self.parents[x] = y
        else:
            self.size[x] += self.size[y]
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
    def group_count(self):
        return len(self.roots())
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
n,m=list(map(int,input().split()))
num=[list(map(int,input().split())) for _ in range(m)]
ans=0
for i in range(m):
    uf=UnionFind(n)
    for j in range(m):
        if i!=j:
            uf.union(num[j][0]-1,num[j][1]-1)
    if uf.size[uf.find(0)]!=n:
        ans+=1
print(ans)

