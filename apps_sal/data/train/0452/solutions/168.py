class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        grid = [[-1] * n for i in range(d)]
        M = sum(jobDifficulty)

        m = 0
        for i in reversed(range(len(grid[0]))):
            m = max(jobDifficulty[i], m)
            grid[0][i] = m

        for i in range(1, d):
            for j in reversed(range(len(grid[i - 1]))):
                m = jobDifficulty[j]
                tmp = M
                got = False
                for k in range(j + 1, len(grid[i - 1])):
                    # print(i, j, k)
                    if grid[i - 1][k] > -1:
                        tmp = min(m + grid[i - 1][k], tmp)
                        got = True
                    m = max(jobDifficulty[k], m)
                if got:
                    grid[i][j] = tmp

        # print(grid)

        return grid[-1][0]
