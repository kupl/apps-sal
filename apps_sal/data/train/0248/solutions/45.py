class Solution:

    def containsCycle(self, grid: List[List[str]]) -> bool:
        (M, N) = (len(grid), len(grid[0]))
        dp = [[set() for j in range(N)] for i in range(M)]
        dv = [(0, -1), (-1, 0)]
        for i in range(M):
            for j in range(N):
                for (x, y) in dv:
                    if 0 <= i + x < M and 0 <= j + y < N:
                        if grid[i][j] == grid[i + x][j + y]:
                            if not dp[i + x][j + y]:
                                dp[i][j].add(((i + x, j + y), 1))
                            else:
                                for entry in dp[i + x][j + y]:
                                    (prnt, dist) = entry
                                    if (prnt, dist + 1) in dp[i][j] and dist + 1 >= 2:
                                        return True
                                    dp[i][j].add((prnt, dist + 1))
        return False
