class UnionFind():
    def __init__(self, n):
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

n,m = map(int,input().split())
a = [list(map(int,input().split())) for i in range(m)]
ans = 0
for i in range(m):
    uf = UnionFind(n+1)
    cnt = 0
    for j in range(m):
        if i == j:
            continue
        else:
            uf.union(a[j][0],a[j][1])
    for k in uf.parents:
        if k < 0:
            cnt += 1
    if cnt != 2:
        ans += 1

print(ans)
