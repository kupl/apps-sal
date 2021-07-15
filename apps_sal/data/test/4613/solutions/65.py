import sys

input = sys.stdin.readline


class UnionFind:
    """Union Find class.

    "Path compression" and "Union by rank" are used.

    References:
        <https://en.wikipedia.org/wiki/Disjoint-set_data_structure>
    """

    def __init__(self, N):
        self.N = N
        self.__make_set()

    def __make_set(self):
        self._parent = list(range(self.N + 1))
        self._rank = [0] * (self.N + 1)
        self._size = [1] * (self.N + 1)

    def find(self, x):
        if self._parent[x] != x:
            self._parent[x] = self.find(self._parent[x])
        return self._parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        x_rank = self._rank[x_root]
        y_rank = self._rank[y_root]
        if x_rank > y_rank:
            self._parent[y_root] = x_root
            self._size[x_root] += self._size[y_root]
        elif x_rank < y_rank:
            self._parent[x_root] = y_root
            self._size[y_root] += self._size[x_root]
        else:
            self._parent[y_root] = x_root
            self._rank[x_root] += 1
            self._size[x_root] += self._size[y_root]

    def same_set(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return self._size[self.find(x)]


def main():
    N, M = list(map(int, input().split()))
    a = [None] * M
    b = [None] * M
    for i in range(M):
        a[i], b[i] = list(map(int, input().split()))

    ans = 0
    for i in range(M):
        uf = UnionFind(N)
        for j in range(M):
            if j == i:
                continue
            uf.union(a[j], b[j])
        if not uf.same_set(a[i], b[i]):
            ans += 1

    print(ans)


def __starting_point():
    main()

__starting_point()
