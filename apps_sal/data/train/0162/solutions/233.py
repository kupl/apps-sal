class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:

        # 注意这里不要写成【0 * （len....）】
        dp_grid = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]

        for r in range(len(s2) + 1):
            for c in range(len(s1) + 1):

                if r == 0 or c == 0:
                    dp_grid[r][c] = 0

                # 注意这里的s2和s1是string,别搞错写成s2[r-1][c-1]了
                elif s2[r - 1] == s1[c - 1]:
                    dp_grid[r][c] = dp_grid[r - 1][c - 1] + 1

                else:
                    dp_grid[r][c] = max(dp_grid[r - 1][c], dp_grid[r][c - 1])

        return dp_grid[-1][-1]
