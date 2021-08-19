class UnionFind:
    def __init__(self, n, t, s):
        self.par = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)
        self.sizex = [1] * t + [0] * s
        self.sizey = [0] * t + [1] * s

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def sizeof(self, x):
        return self.sizex[self.find(x)] * self.sizey[self.find(x)]

    # 併合
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.sizex[y] += self.sizex[x]
            self.sizey[y] += self.sizey[x]
        else:
            self.par[y] = x
            self.sizex[x] += self.sizex[y]
            self.sizey[x] += self.sizey[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)


def coordinate_compression(arr):
    return {v: k for k, v in enumerate(sorted(set(arr)))}


n = int(input())
x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = list(map(int, input().split()))
dx = coordinate_compression(x)
dy = coordinate_compression(y)
uf = UnionFind(len(dx) + len(dy), len(dx), len(dy))
for i in range(n):
    uf.unite(dx[x[i]], dy[y[i]] + len(dx))
s = set()
ans = 0
for i in range(len(dx)):
    p = uf.find(i)
    if p in s:
        continue
    ans += uf.sizeof(i)
    s.add(p)
print((ans - n))
