from typing import List


class DSU:
    def __init__(self, n: int = 0) -> None:
        self._n: int = n
        # root node: -1 * component size
        # otherwise: parent
        self.parent_or_size: List[int] = [-1] * n

    def merge(self, a: int, b: int) -> int:
        assert 0 <= a < self._n
        assert 0 <= b < self._n
        x, y = self.leader(a), self.leader(b)
        if x == y:
            return x
        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x
        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x
        return x

    def same(self, a: int, b: int) -> bool:
        assert 0 <= a < self._n
        assert 0 <= b < self._n
        return self.leader(a) == self.leader(b)

    def leader(self, a: int) -> int:
        assert 0 <= a < self._n
        if self.parent_or_size[a] < 0:
            return a
        self.parent_or_size[a] = self.leader(self.parent_or_size[a])
        return self.parent_or_size[a]


N, M, *AB = list(map(int, open(0).read().split()))
d = DSU(N)
for a, b in zip(*[iter(AB)] * 2):
    d.merge(a - 1, b - 1)
print((-min(d.parent_or_size)))
