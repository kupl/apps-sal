class Solution:

    def regionsBySlashes(self, grid: List[str]) -> int:
        for i in range(len(grid)):
            grid[i] = grid[i].replace('\\\\', '*')
        N = len(grid)
        record = [[[0, 0, 0, 0] for j in range(N)] for i in range(N)]
        count = 0

        def dfs(i, j, k):
            if 0 <= i < N and 0 <= j < N and (record[i][j][k] == 0):
                if grid[i][j] == '*':
                    if k <= 1:
                        record[i][j][0] = record[i][j][1] = count
                        dfs(i - 1, j, 2)
                        dfs(i, j + 1, 3)
                    else:
                        record[i][j][2] = record[i][j][3] = count
                        dfs(i + 1, j, 0)
                        dfs(i, j - 1, 1)
                elif grid[i][j] == '/':
                    if 1 <= k <= 2:
                        record[i][j][1] = record[i][j][2] = count
                        dfs(i + 1, j, 0)
                        dfs(i, j + 1, 3)
                    else:
                        record[i][j][0] = record[i][j][3] = count
                        dfs(i - 1, j, 2)
                        dfs(i, j - 1, 1)
                else:
                    record[i][j][0] = record[i][j][1] = record[i][j][2] = record[i][j][3] = count
                    dfs(i - 1, j, 2)
                    dfs(i, j + 1, 3)
                    dfs(i + 1, j, 0)
                    dfs(i, j - 1, 1)
        for i in range(N):
            for j in range(N):
                for k in range(4):
                    if record[i][j][k] == 0:
                        count += 1
                        dfs(i, j, k)
        return count
