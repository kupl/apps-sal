class Unionset:
    def __init__(self, N):
        self.parent = [x for x in range(N)]
        self.rank = [0 for x in range(N)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xx = self.find(x)
        yy = self.find(y)
        if self.parent[xx] == self.parent[yy]:
            return True
        if self.rank[xx] > self.rank[yy]:
            self.parent[yy] = self.parent[xx]
        elif self.rank[xx] < self.rank[yy]:
            self.parent[xx] = self.parent[yy]
        else:
            self.rank[xx] += 1
            self.parent[yy] = self.parent[xx]
        return False


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        ds = Unionset(n * n * 4)
        # print(ds.parent)
        for r in range(n):
            for c in range(n):
                root = 4 * (r * n + c)
                if grid[r][c] == '/':
                    ds.union(root, root + 1)
                    ds.union(root + 2, root + 3)
                elif grid[r][c] == '\\\\':
                    ds.union(root, root + 2)
                    ds.union(root + 1, root + 3)
                else:
                    ds.union(root, root + 1)
                    ds.union(root + 1, root + 2)
                    ds.union(root + 2, root + 3)
                # print(grid[r][c])
                # print(\"first\",ds.parent)
                if r + 1 < n:
                    ds.union(root + 3, root + (4 * n))
                if c + 1 < n:
                    ds.union(root + 2, root + 5)
                # print(\"second\",ds.parent)
        tot = 0
        for i in range(4 * n * n):
            if ds.find(i) == i:
                tot += 1
        return tot
