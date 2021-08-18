class UnionFind:
    def __init__(self, n=1):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.parent[y] = x

    def is_same(self, x, y):
        return self.find(x) == self.find(y)


N = int(input())
uf = UnionFind(N)
X = []
Y = []
for i in range(N):
    x, y = map(int, input().split())
    X.append((x, i))
    Y.append((y, i))

X.sort()
Y.sort()
road = []


def add_cand(Z):
    nonlocal road
    z1, i1 = Z[0]
    for j in range(1, N):
        z2, i2 = Z[j]
        road.append((z2 - z1, i1, i2))
        z1, i1 = z2, i2


add_cand(X)
add_cand(Y)

road.sort()
ans = 0
for cost, i, j in road:
    if uf.is_same(i, j):
        continue
    uf.union(i, j)
    ans += cost

print(ans)
