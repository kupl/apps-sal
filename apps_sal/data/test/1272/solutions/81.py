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

n,m=map(int,input().split())
e=[list(map(int,input().split())) for _ in range(m)][::-1]
u=UnionFind(n)
tmp=n*(n-1)//2
ans=[]
for a,b in e:
    ans.append(tmp)
    a,b=a-1,b-1
    if u.same(a,b):
        continue
    tmp-=u.size(a)*u.size(b)
    u.union(a,b)
print(*ans[::-1],sep='\n')
