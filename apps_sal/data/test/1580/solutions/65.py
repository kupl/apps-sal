class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1]*n
        self.rank = [0]*n

    def find(self, x):
        if self.root[x-1] < 0:
            return x
        else:
            self.root[x-1] = self.find(self.root[x-1])
            return self.root[x-1]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x==y:
            return
        elif self.rank[x-1] > self.rank[y-1]:
            self.root[x-1] += self.root[y-1]
            self.root[y-1] = x
            self.n-=1
        else:
            self.n-=1
            self.root[y-1] += self.root[x-1]
            self.root[x-1] = y
            if self.rank[x-1] == self.rank[y-1]:
                self.rank[y-1] += 1

    def same(self, x, y):
        return self.find(x)==self.find(y)

    def count(self, x):
        return -self.root[self.find(x)-1]
    def num(self):
        return self.n

N,M=list(map(int,input().split()))
uf=UnionFind(N)
for i in range(M):
    x,y,z=list(map(int,input().split()))
    uf.unite(x,y)
print((uf.num()))

