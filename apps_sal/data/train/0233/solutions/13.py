class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        parent = {}
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            parent[rx] = ry
            return True
        
        res = m * n * 4
        for i in range(m):
            for j in range(n):
                for k in range(4):
                    parent[(i, j, k)] = (i, j, k)
                if grid[i][j] == '/':
                    if union((i, j, 0), (i, j, 3)):
                        res -= 1
                    if union((i, j, 1), (i, j, 2)):
                        res -= 1
                elif grid[i][j] == '\\\\':
                    if union((i, j, 0), (i, j, 1)):
                        res -= 1
                    if union((i, j, 2), (i, j, 3)):
                        res -= 1
                else:
                    if union((i, j, 0), (i, j, 1)):
                        res -= 1
                    if union((i, j, 2), (i, j, 3)):
                        res -= 1
                    if union((i, j, 0), (i, j, 3)):
                        res -= 1
                
                if i > 0:
                    if union((i, j, 0), (i - 1, j, 2)):
                        res -= 1
                if j > 0:
                    if union((i, j, 3), (i, j - 1, 1)):
                        res -= 1
        return res
