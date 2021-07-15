class UnionFind:
    def __init__(self, m: int, n: int):
        self.rank = collections.Counter()
        self.parent = {(i, j): (i, j) for i in range(m) for j in range(n)}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        if self.rank[py] > self.rank[px]:
            px, py = py, px
        if self.rank[py] == self.rank[px]:
            self.rank[px] += 1
        self.parent[py] = px
        
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        uf = UnionFind(rows, cols)
        for i, row in enumerate(grid):
            for j, letter in enumerate(row):
                if (i > 0 and j > 0 and
                        grid[i - 1][j] == grid[i][j - 1] == letter and
                        uf.find((i - 1, j)) == uf.find((i, j - 1))):
                    return True
                for r, c in (i - 1, j), (i, j - 1):
                    if 0 <= r and 0 <= c and grid[r][c] == letter:
                        uf.union((i, j), (r, c))
        return False


