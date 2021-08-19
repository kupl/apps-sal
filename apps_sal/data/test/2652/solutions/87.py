n = int(input())
l = sorted([list(map(int, input().split())) + [i] for i in range(n)])
xs = [(x, i)for x, y, i in l]
ys = sorted([(x, i)for y, x, i in l])
edges = {}
for i in range(1, n):
    a, s = xs[i - 1]
    d, f = xs[i]
    if (s, f) in edges:
        edges[(s, f)] = min(edges[(s, f)], abs(a - d))
    else:
        edges[(s, f)] = abs(a - d)
    a, s = ys[i - 1]
    d, f = ys[i]
    if (s, f) in edges:
        edges[(s, f)] = min(edges[(s, f)], abs(a - d))
    else:
        edges[(s, f)] = abs(a - d)
edges = sorted(edges.items(), key=lambda x: x[1])


class UnionFind:
    # def   -> foo=UnionFind(n,1)  <- 1-based index, default is 0
    # method -> foo.hoge(huga)
    __slots__ = ["_size", "_first_idx", "_parents"]

    def __init__(self, size: int, first_index: int = 0) -> None:
        self._size = size
        self._first_idx = first_index
        self._parents = [-1] * (size + first_index)

    def find(self, x: int) -> int:
        if self._parents[x] < 0:
            return x
        self._parents[x] = self.find(self._parents[x])
        return self._parents[x]

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def unite(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self._parents[x] > self._parents[y]:
            x, y = y, x
        self._parents[x] += self._parents[y]
        self._parents[y] = x
        return True

    def size(self, x: int) -> int:
        return -self._parents[self.find(x)]

    def group_count(self) -> int:
        return sum(1 for i in self._parents if i < 0) - self._first_idx

    def connected(self) -> bool:
        return self._parents[self.find(self._first_idx)] == -self._size


uf = UnionFind(n)
ans = edges[0][1]
uf.unite(*edges[0][0])
for f, c in edges:
    if uf.same(*f):
        continue
    uf.unite(*f)
    ans += c
print(ans)
