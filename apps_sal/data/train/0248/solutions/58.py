class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def ff(grid, i, j, n, c):
            grid[i][j] = c
            c += 1
            if i > 0:
                # print(grid)
                if type(grid[i - 1][j]) == int and c - grid[i - 1][j] > 2 and c // 250000 == grid[i - 1][j] // 250000:
                    return True
                elif type(grid[i - 1][j]) == str and grid[i - 1][j] == n:

                    # print(grid)
                    if ff(grid, i - 1, j, n, c):
                        return True
            if j < len(grid[i]) - 1:
                # print(grid)
                if type(grid[i][j + 1]) == int and c - grid[i][j + 1] > 2 and c // 250000 == grid[i][j + 1] // 250000:
                    return True
                elif type(grid[i][j + 1]) == str and grid[i][j + 1] == n:

                    if ff(grid, i, j + 1, n, c):
                        return True
            if j > 0:
                # print(grid,n)
                if type(grid[i][j - 1]) == int and c - grid[i][j - 1] > 2 and c // 250000 == grid[i][j - 1] // 250000:
                    return True
                elif type(grid[i][j - 1]) == str and grid[i][j - 1] == n:

                    if ff(grid, i, j - 1, n, c):
                        return True
            if i < len(grid) - 1:
                # print(grid,n)

                if type(grid[i + 1][j]) == int and c - grid[i + 1][j] > 2 and c // 250000 == grid[i + 1][j] // 250000:
                    return True
                elif type(grid[i + 1][j]) == str and grid[i + 1][j] == n:
                    # print(grid)

                    if ff(grid, i + 1, j, n, c):
                        return True
            return False
        cc = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if type(grid[i][j]) != int:
                    cc += 1
                    if ff(grid, i, j, grid[i][j], cc * 250000):
                        return True
        return False
