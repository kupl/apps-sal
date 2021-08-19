class Solution:

    def containsCycle(self, grid: List[List[str]]) -> bool:
        (row, col) = (len(grid), len(grid[0]))
        track = {}
        (dx, dy) = ([0, 0, -1, 1], [-1, 1, 0, 0])

        def check(i, j, parent):
            for k in range(4):
                (xx, yy) = (dx[k] + i, dy[k] + j)
                if xx in range(row) and yy in range(col) and (parent != (xx, yy)) and (grid[i][j] == grid[xx][yy]) and (grid[i][j] != 'checked'):
                    if (xx, yy) in track:
                        return True
                    track[xx, yy] = True
                    if check(xx, yy, (i, j)):
                        return True
                    grid[xx][yy] = 'checked'
            return False
        for i in range(row):
            for j in range(col):
                track[i, j] = True
                if check(i, j, None):
                    return True
                grid[i][j] = 'checked'
        return False
