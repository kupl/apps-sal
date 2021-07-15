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

n,m,k=map(int,input().split())
friend=[[] for _ in range(n)]
block=[[] for _ in range(n)]
a=UnionFind(n)
for i in range(m):
    x,y=map(int,input().split())
    friend[x-1].append(y-1)
    friend[y-1].append(x-1)
    a.union(x-1,y-1)
for i in range(k):
    x,y=map(int,input().split())
    block[x-1].append(y-1)
    block[y-1].append(x-1)
ans=[]
for i in range(n):
    ans.append(a.size(i)-len(friend[i])-sum(a.same(i,j) for j in block[i])-1)
print(*ans)
