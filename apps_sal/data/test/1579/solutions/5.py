class UnionFind:
    def __init__(self, N):
        self.p = list(range(N))
        self.rank = [0] * N
        self.size = [1] * N

    def find_root(self, x):
        if self.p[x] != x:
            self.p[x] = self.find_root(self.p[x])

        return self.p[x]

    def same(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def unite(self, x, y):
        u = self.find_root(x)
        v = self.find_root(y)

        if u == v:
            return

        if self.rank[u] < self.rank[v]:
            self.p[u] = v
            self.size[v] += self.size[u]
            self.size[u] = 0
        else:
            self.p[v] = u
            self.size[u] += self.size[v]
            self.size[v] = 0

            if self.rank[u] == self.rank[v]:
                self.rank[u] += 1

    def get_size(self, x):
        return self.size[self.find_root(x)]


n = int(input())
xy = [tuple(int(x) for x in input().split()) for _ in range(n)]

sx = set()
sy = set()

for x, y in xy:
    sx.add(x)
    sy.add(y)

dx = dict()
dy = dict()

for i, x in enumerate(sx):
    dx[x] = i

len_x = len(sx)
m = len(sx) + len(sy)

for i, y in enumerate(sy):
    dy[y] = i + len_x


uft = UnionFind(m)

for x, y in xy:
    uft.unite(dx[x], dy[y])

mx = [0] * m
my = [0] * m
for i in range(len_x):
    mx[uft.find_root(i)] += 1
for i in range(len_x, m):
    my[uft.find_root(i)] += 1

ans = 0
for i in range(m):
    ans += mx[i] * my[i]

print(ans - n)
