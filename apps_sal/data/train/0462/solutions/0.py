class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        xbucket, ybucket, server = [0] * len(grid), [0] * len(grid[0]), []
        for x, row in enumerate(grid):
            for y, cell in enumerate(row):
                if cell:
                    server.append((x, y))
                    xbucket[x] += 1
                    ybucket[y] += 1
        return sum(xbucket[x] > 1 or ybucket[y] > 1 for x, y in server)
