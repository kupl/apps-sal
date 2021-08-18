from typing import Set


class UnionFind:
    """Union-Find: O(α(N))"""

    __slots__ = ["_data_size", "_first_idx", "_parents"]

    def __init__(self, data_size: int, is_zero_origin: bool = True) -> None:
        self._data_size = data_size
        self._first_idx = 0 if is_zero_origin else 1
        self._parents = [-1] * (data_size + self._first_idx)

    def __getitem__(self, x: int) -> int:
        """Find the group (root) of vertex x."""
        if self._parents[x] < 0:
            return x
        self._parents[x] = self[self._parents[x]]
        return self._parents[x]

    def __len__(self) -> int:
        """Count the number of groups (roots)."""
        return len(self.groups)

    @property
    def groups(self) -> Set[int]:
        """Return the set of groups (roots)."""
        return {
            self[x] for x in range(self._first_idx, self._data_size + self._first_idx)
        }

    def is_connected(self, x: int, y: int) -> bool:
        """Return whether two vertices x and y are connected or not."""
        return self[x] == self[y]

    def unite(self, x: int, y: int) -> None:
        """Unite two groups of vertices x and y."""
        x, y = self[x], self[y]
        if x == y:
            return
        if self._parents[x] > self._parents[y]:
            x, y = y, x
        self._parents[x] += self._parents[y]
        self._parents[y] = x


def main():
    N, _, *X = list(map(int, open(0).read().split()))
    tree = UnionFind(N, is_zero_origin=False)
    for x, y, _ in zip(*[iter(X)] * 3):
        tree.unite(x, y)
    print((len(tree)))


def __starting_point():
    main()


__starting_point()
