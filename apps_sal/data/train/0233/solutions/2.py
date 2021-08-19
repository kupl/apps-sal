from typing import List


class DS:

    def __init__(self, n):
        self.sizes = [1] * n
        self.roots = [i for i in range(n)]

    def query(self, x):
        root = x
        while root != self.roots[root]:
            self.roots[root] = self.roots[self.roots[root]]
            root = self.roots[root]
        return root

    def union(self, x, y):
        (xRoot, yRoot) = (self.query(x), self.query(y))
        (s, l) = (xRoot, yRoot) if self.sizes[xRoot] < self.sizes[yRoot] else (yRoot, xRoot)
        self.roots[s] = l
        self.sizes[l] += self.sizes[s]


class Solution:

    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        nodes = DS(4 * n * n)

        def getIndex(r, c, k):
            return 4 * (n * r + c) + k
        for i in range(n):
            for j in range(n):
                if i > 0:
                    nodes.union(getIndex(i, j, 0), getIndex(i - 1, j, 2))
                if i < n - 1:
                    nodes.union(getIndex(i, j, 2), getIndex(i + 1, j, 0))
                if j > 0:
                    nodes.union(getIndex(i, j, 3), getIndex(i, j - 1, 1))
                if j < n - 1:
                    nodes.union(getIndex(i, j, 1), getIndex(i, j + 1, 3))
                if grid[i][j] != '/':
                    nodes.union(getIndex(i, j, 0), getIndex(i, j, 1))
                    nodes.union(getIndex(i, j, 3), getIndex(i, j, 2))
                if grid[i][j] != '\\\\':
                    nodes.union(getIndex(i, j, 0), getIndex(i, j, 3))
                    nodes.union(getIndex(i, j, 1), getIndex(i, j, 2))
        return sum((i == nodes.query(i) for i in range(4 * n * n)))
