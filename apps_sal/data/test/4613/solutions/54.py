class union_find():
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)


n, m = map(int, input().split())
uf = union_find(n)
ans = 0
s = []
for _ in range(m):
    a = list(map(int, input().split()))
    s.append(a)
    uf.union(a[0], a[1])


for e in range(m):
    uf1 = union_find(n)
    ch = 0
    for d in range(m):
        if d != e:
            uf1.union(s[d][0], s[d][1])

    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if not uf1.same(i, j):
                ch += 1
    if ch > 0:
        ans += 1


print(ans)
