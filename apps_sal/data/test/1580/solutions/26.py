from collections import Counter
import sys
input = sys.stdin.readline


def read():
    N, M = list(map(int, input().strip().split()))
    XYZ = []
    for i in range(M):
        x, y, z = list(map(int, input().strip().split()))
        XYZ.append((x, y, z))
    return N, M, XYZ


class UnionFind():
    """Union-Find木の実装
    """

    def __init__(self, n):
        self.n = n
        self.parent = [x for x in range(n)]

    def find(self, x):
        """要素xが所属するグループを返す
        """
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        """要素x, yがそれぞれ所属するグループを併合する
        """
        x = self.find(x)
        y = self.find(y)
        if x > y:
            x, y = y, x
        self.parent[y] = x

    def parents(self):
        return [self.find(x) for x in range(self.n)]


def solve(N, M, XYZ):
    uf = UnionFind(N)
    for x, y, z in XYZ:
        uf.union(x - 1, y - 1)
    C = Counter(uf.parents())
    return len(C)


def __starting_point():
    inputs = read()
    print((solve(*inputs)))


__starting_point()
