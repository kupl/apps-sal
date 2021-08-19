(n, m) = list(map(int, input().split()))
xy = []
for _ in range(m):
    (x, y, _) = list(map(int, input().split()))
    xy.append((x - 1, y - 1))


class UF:

    def __init__(self, n):
        self.n = n
        self.g = list(range(n))
        self.vertices = list(range(n))

    def union(self, i0, i1):
        (g0, g1) = (self.find(i0), self.find(i1))
        (g0, g1) = (min(g0, g1), max(g0, g1))
        self.g[g1] = g0

    def find(self, i):
        path = []
        while self.g[i] != i:
            path.append(i)
            i = self.g[i]
        for j in path:
            self.g[j] = i
        return i


uf = UF(n)
for (x, y) in xy:
    uf.union(x, y)
g = set()
for x in range(n):
    g.add(uf.find(x))
answer = len(g)
print(answer)
