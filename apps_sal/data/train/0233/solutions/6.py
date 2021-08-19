class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        print(m, n)
        mat = [[0] * (4 * n) for _ in range(4 * m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '/':
                    mat[4 * i][4 * j + 3] = 1
                    mat[4 * i + 1][4 * j + 2] = 1
                    mat[4 * i + 2][4 * j + 1] = 1
                    mat[4 * i + 3][4 * j] = 1
                elif grid[i][j] == '\\\\':
                    mat[4 * i][4 * j] = 1
                    mat[4 * i + 1][4 * j + 1] = 1
                    mat[4 * i + 2][4 * j + 2] = 1
                    mat[4 * i + 3][4 * j + 3] = 1
        # print(mat)
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def dfs(i, j):
            visit[i][j] = 1
            for d in dirs:
                x, y = i + d[0], j + d[1]
                if 0 <= x < (4 * m) and 0 <= y < (4 * n) and not mat[x][y]:
                    mat[x][y] = 1
                    if not visit[x][y]:
                        dfs(x, y)

        visit = [[0] * (4 * n) for _ in range(4 * m)]
        res = 0
        for i in range(4 * m):
            for j in range(4 * n):
                if not mat[i][j]:
                    res += 1
                    dfs(i, j)
        return res
