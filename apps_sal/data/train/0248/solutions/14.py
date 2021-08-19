class Solution:
    x = [0, 0, -1, 1]
    y = [-1, 1, 0, 0]

    def findCycle(self, grid, i, j, li, lj, path, vis):
        if vis[i][j]:
            return False
        for k in range(4):
            nx = i + Solution.x[k]
            ny = j + Solution.y[k]
            if nx == li and ny == lj:
                continue
            if nx < 0 or ny < 0 or nx >= len(grid) or (ny >= len(grid[0])):
                continue
            if (nx, ny) in path and path[nx, ny] == 1:
                vis[i][j] = 1
                return True
            if grid[nx][ny] == grid[i][j]:
                path[nx, ny] = 1
                isfind = self.findCycle(grid, nx, ny, i, j, path, vis)
                if isfind:
                    vis[i][j] = 1
                    return True
                path[nx, ny] = 0
        vis[i][j] = 1
        return False

    def containsCycle(self, grid: List[List[str]]) -> bool:
        h = len(grid)
        if h == 0:
            return False
        w = len(grid[0])
        vis = [[0 for i in range(w)] for j in range(h)]
        path = {}
        for i in range(h):
            for j in range(w):
                if not vis[i][j]:
                    isfind = self.findCycle(grid, i, j, -1, -1, path, vis)
                    if isfind:
                        return True
        return False
