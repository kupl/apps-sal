class UnionFind():
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n

    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                self.par[x] = y
            else:
                self.par[y] = x
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1

    def samegrp(self, x, y):
        return self.root(x) == self.root(y)

n, m = [int(x) for x in input().split()]
A = UnionFind(n)
ans = n
for i in range(m):
    x, y, _ = [int(z) - 1 for z in input().split()]
    if not A.samegrp(x, y):
        ans -=1
    A.union(x, y)

print(ans)

