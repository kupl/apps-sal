from collections import defaultdict
n, k, l = map(int, input().split())


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
        news = []
        p = self._parents
        y = p[x]
        while y >= 0:
            news.append(x)
            x, y = y, p[y]
        if len(news) != 1:
            for P in news:
                p[P] = x
        return x

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


road = UnionFind(1, n)
rail = UnionFind(1, n)

for i in range(k):
    road.unite(*map(int, input().split()))
for i in range(l):
    rail.unite(*map(int, input().split()))
d = defaultdict(int)

for i in range(1, n + 1):
    ap, op = rail.find(i), road.find(i)
    d[ap * (n + 1) + op] += 1
print(*[d[road.find(i) + rail.find(i) * (n + 1)]for i in range(1, n + 1)])
