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
            self.n-=1
            self.root[x-1] += self.root[y-1]
            self.root[y-1] = x
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

    def size(self):
        return self.n

    def roots(self):
        return [x+1 for x in range(n) if self.root[x] < 0]

mod=998244353
n,K=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(n)]

r=UnionFind(n)
c=UnionFind(n)
for i in range(n):
    for j in range(i+1,n):
        pr,pc=True,True
        for k in range(n):
            if A[i][k]+A[j][k]>K:
                pr=False
            if A[k][i]+A[k][j]>K:
                pc=False
        if pr: r.unite(i+1,j+1)
        if pc: c.unite(i+1,j+1)
p=[1]*(n+1)
for i in range(1,n+1):
    p[i]=(p[i-1]*i)%mod
ans=1
for x in r.roots():
    ans=ans*p[-r.root[x-1]]%mod
for x in c.roots():
    ans=ans*p[-c.root[x-1]]%mod
print(ans)
