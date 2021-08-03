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


n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

abb = ab[::-1]
uf = UnionFind(n)

ini = (n * (n - 1)) // 2
res = [ini]
temp = 0
for i in range(m - 1):
    a = abb[i][0] - 1
    b = abb[i][1] - 1
    ax = uf.size(a)
    bx = uf.size(b)
    if uf.same(a, b):
        pass
    else:
        uf.union(a, b)
        temp += ax * bx
    res.append(ini - temp)

ress = res[::-1]
for i in range(m):
    print(ress[i])
