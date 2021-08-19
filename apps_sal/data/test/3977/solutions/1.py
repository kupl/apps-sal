class DisjointSet:

    def __init__(self, n):
        self._n = n
        self._size = [1 for _ in range(n)]
        self._depth = [0 for _ in range(n)]
        self._root = [u for u in range(n)]

    def root(self, u):
        if self._root[u] != u:
            self._root[u] = self.root(self._root[u])
        return self._root[u]

    def join(self, u, v):
        rootU = self.root(u)
        rootV = self.root(v)
        if rootU == rootV:
            return
        if self._depth[rootU] < self._depth[rootV]:
            self._root[rootU] = rootV
            self._size[rootV] += self._size[rootU]
        else:
            self._root[rootU] = rootV
            self._size[rootV] += self._size[rootU]

    def size(self, u):
        return self._size[u]

    def roots(self):
        return [u for u in range(self._n) if self._root[u] == u]


def ReadMany():
    return list(map(int, input().split()))


def SubtractOne(c):
    return [x - 1 for x in c]


def C2(n):
    return n * (n - 1) // 2


(n, m, k) = ReadMany()
c = list(SubtractOne(ReadMany()))
degree = [0 for _ in range(n)]
ds = DisjointSet(n)
for i in range(m):
    (u, v) = SubtractOne(ReadMany())
    ds.join(u, v)
    degree[u] += 1
    degree[v] += 1
ccDegree = [0 for _ in range(n)]
for u in range(n):
    ccDegree[ds.root(u)] += degree[u]
cRoots = list(map(ds.root, c))
biggestCRoot = max(list(map(ds.size, cRoots)))
answer = 0
for u in ds.roots():
    answer += C2(ds.size(u)) - ccDegree[u] // 2
    if u not in cRoots:
        answer += ds.size(u) * biggestCRoot
        biggestCRoot += ds.size(u)
print(answer)
