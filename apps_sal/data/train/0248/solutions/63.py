class Solution:

    def containsCycle(self, grid: List[List[str]]) -> bool:
        if not grid:
            return False
        (m, n) = (len(grid), len(grid[0]))
        nbrs = [(-1, 0), (0, 1), (0, -1), (1, 0)]

        def isValid(x, y):
            return x >= 0 and x < m and (y >= 0) and (y < n)

        def hasCycle(x, y, vis, parentX, parentY):
            vis.add((x, y))
            for nbr in nbrs:
                (newX, newY) = (x + nbr[0], y + nbr[1])
                if isValid(newX, newY) and grid[newX][newY] == grid[x][y] and (not (parentX == newX and parentY == newY)):
                    if (newX, newY) in vis:
                        return True
                    elif hasCycle(newX, newY, vis, x, y):
                        return True
            return False
        vis = set()
        for i in range(m):
            for j in range(n):
                if (i, j) not in vis:
                    ans = hasCycle(i, j, vis, -1, -1)
                if ans:
                    return True
        return False
