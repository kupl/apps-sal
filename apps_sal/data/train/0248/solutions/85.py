class DSU:

    def __init__(self, n):
        self.par = list(range(n))
        self.count = [1] * n

    def find(self, u):
        if u != self.par[u]:
            self.par[u] = self.find(self.par[u])
        return self.par[u]

    def union(self, u, v):
        (p1, p2) = (self.find(u), self.find(v))
        if p1 == p2:
            return False
        if self.count[p1] < self.count[p2]:
            (p1, p2) = (p2, p1)
        self.count[p1] += self.count[p2]
        self.count[p2] = self.count[p1]
        self.par[p2] = p1
        return True


class Solution:

    def containsCycle(self, grid: List[List[str]]) -> bool:
        (m, n) = (len(grid), len(grid[0]))
        dsu = DSU(m * n)
        for i in range(m):
            for j in range(n):
                for (p, q) in [(i + 1, j), (i, j + 1)]:
                    if 0 <= p < m and 0 <= q < n and (grid[i][j] == grid[p][q]):
                        if not dsu.union(i * n + j, p * n + q):
                            return True
        print(dsu.count)
        return False
