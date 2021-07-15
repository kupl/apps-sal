class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        self.res = math.inf
        grid = [[False] * n for _ in range(m)]

        def dfs(i, j, s):
            if s >= self.res:
                return
            elif i == m:
                self.res = s
            elif j == n:
                dfs(i + 1, 0, s)
            elif grid[i][j]:
                dfs(i, j + 1, s)
            else:
                side = min(m - i, n - j)
                while side:
                    if not any(
                        grid[ni][nj]
                        for ni in range(i, i + side)
                        for nj in range(j, j + side)
                    ):
                        for ni in range(i, i + side):
                            for nj in range(j, j + side):
                                grid[ni][nj] = True
                        dfs(i, j + side, s + 1)
                        for ni in range(i, i + side):
                            for nj in range(j, j + side):
                                grid[ni][nj] = False
                    side -= 1

        dfs(0, 0, 0)
        return self.res
