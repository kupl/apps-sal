class Solution:

    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        seen = [[[0, 0, 0, 0] for x in range(n)] for y in range(n)]

        def dfs(x, y, loc):
            if not (0 <= x < n and 0 <= y < n) or seen[x][y][loc] == 1:
                return
            seen[x][y][loc] = 1
            if grid[x][y] == '/':
                if loc == 0:
                    dfs(x + 1, y, 2)
                    seen[x][y][3] = 1
                    dfs(x, y + 1, 1)
                elif loc == 3:
                    dfs(x, y + 1, 1)
                    seen[x][y][0] = 1
                    dfs(x + 1, y, 2)
                elif loc == 1:
                    dfs(x, y - 1, 3)
                    seen[x][y][2] = 1
                    dfs(x - 1, y, 0)
                else:
                    dfs(x - 1, y, 0)
                    seen[x][y][1] = 1
                    dfs(x, y - 1, 3)
            elif grid[x][y] == '\\\\':
                if loc == 0:
                    dfs(x + 1, y, 2)
                    seen[x][y][1] = 1
                    dfs(x, y - 1, 3)
                elif loc == 3:
                    dfs(x, y + 1, 1)
                    seen[x][y][2] = 1
                    dfs(x - 1, y, 0)
                elif loc == 1:
                    dfs(x, y - 1, 3)
                    seen[x][y][0] = 1
                    dfs(x + 1, y, 2)
                else:
                    dfs(x - 1, y, 0)
                    seen[x][y][3] = 1
                    dfs(x, y + 1, 1)
            else:
                seen[x][y][1] = 1
                dfs(x, y - 1, 3)
                seen[x][y][2] = 1
                dfs(x - 1, y, 0)
                seen[x][y][0] = 1
                dfs(x + 1, y, 2)
                seen[x][y][3] = 1
                dfs(x, y + 1, 1)
        count = 0
        for i in range(n):
            for j in range(n):
                for loc in range(4):
                    k = seen[i][j][loc]
                    if k == 0:
                        count += 1
                        dfs(i, j, loc)
        return count
