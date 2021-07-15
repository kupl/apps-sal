class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        parent = {}

        def find(u):
            parent.setdefault(u, u)
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            x, y = find(u), find(v)
            if x != y:
                parent[y] = x 
            return x != y

        m, n = len(grid), len(grid[0])
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if i + 1 < m and grid[i][j] == grid[i + 1][j]:
                    if not union((i, j), (i + 1, j)):
                        return True
                if j + 1 < n and grid[i][j] == grid[i][j + 1]:
                    if not union((i, j), (i, j + 1)):
                        return True 
        return False
