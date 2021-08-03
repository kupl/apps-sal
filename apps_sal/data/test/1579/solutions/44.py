V = 10**5 + 5


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        # use for n=2*V
        self.xSize = [1 if i < V else 0 for i in range(n)]
        self.ySize = [0 if i < V else 1 for i in range(n)]

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            parentx = self.find(self.parent[x])
            self.parent[x] = parentx
            return parentx

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return
        if self.rank[rootx] > self.rank[rooty]:
            self.parent[rooty] = rootx
            self.xSize[rootx] += self.xSize[rooty]
            self.ySize[rootx] += self.ySize[rooty]
        else:
            self.parent[rootx] = rooty
            self.xSize[rooty] += self.xSize[rootx]
            self.ySize[rooty] += self.ySize[rootx]
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rooty] += 1


n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]
uf = UnionFind(V * 2)
for xi, yi in xy:
    uf.union(xi, yi + V)

# for i in range(V*2):
#     uf.find(i)

ans = 0
used = set()
for i in range(V * 2):
    rooti = uf.find(i)
    if rooti not in used:
        used.add(rooti)
        ans += uf.xSize[rooti] * uf.ySize[rooti]
print((ans - n))
