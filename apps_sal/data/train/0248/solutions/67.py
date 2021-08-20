class Solution:

    def isCycle(self, grid, r, c, visited, pr, pc):
        (nrow, ncol) = (len(grid), len(grid[0]))
        direcs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        visited.add((r, c))
        for (dr, dc) in direcs:
            (nr, nc) = (r + dr, c + dc)
            if 0 <= nr < nrow and 0 <= nc < ncol and (grid[nr][nc] == grid[r][c]) and (not (pr == nr and pc == nc)):
                if (nr, nc) in visited:
                    return True
                if self.isCycle(grid, nr, nc, visited, r, c):
                    return True
        return False

    def containsCycle(self, grid: List[List[str]]) -> bool:
        (nrow, ncol) = (len(grid), len(grid[0]))
        visited = set()
        for r in range(nrow):
            for c in range(ncol):
                if (r, c) in visited:
                    continue
                if self.isCycle(grid, r, c, visited, -1, -1):
                    return True
        return False
