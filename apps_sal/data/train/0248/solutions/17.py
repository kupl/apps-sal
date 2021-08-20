import collections


class Solution:

    def containsCycle(self, grid):
        if not grid:
            return False
        M = len(grid)
        N = len(grid[0])
        parent = {}

        def find(x, y):
            if parent[x, y] != (x, y):
                parent[x, y] = find(parent[x, y][0], parent[x, y][1])
            return parent[x, y]

        def union(x1, y1, x2, y2):
            p1 = find(x1, y1)
            p2 = find(x2, y2)
            if p1 == p2:
                return True
            parent[p1] = p2
            return False

        def move(x, y, grid):
            for (i, j) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= i < M and 0 <= j < N:
                    yield (i, j)
        seen = set()
        for i in range(M):
            for j in range(N):
                seen.add((i, j))
                for (x1, y1) in move(i, j, grid):
                    if (i, j) not in parent:
                        parent[i, j] = (i, j)
                    if (x1, y1) not in parent:
                        parent[x1, y1] = (x1, y1)
                    if grid[i][j] == grid[x1][y1] and (x1, y1) not in seen:
                        if union(i, j, x1, y1):
                            return True
        return False
