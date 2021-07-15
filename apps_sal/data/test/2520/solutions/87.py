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

n,m,k=map(int,input().split())
uf=UnionFind(n)
friend=[[] for _ in range(n)]
brock=[[] for _ in range(n)]
ans=[]
for _ in range(m):
    a,b=map(int,input().split())
    friend[a-1].append(b-1)
    friend[b-1].append(a-1)
    uf.union(a-1,b-1)
for _ in range(k):
    c,d=map(int,input().split())
    brock[c-1].append(d-1)
    brock[d-1].append(c-1)
for i in range(n):
    ans.append(uf.size(i)-len(friend[i])-sum([uf.same(i,j) for j in brock[i]])-1)
print(*ans)
