class Solution:
    def knightDialer(self, n: int) -> int:
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]
        R, C = len(grid), len(grid[0])
        dp = [[1] * C for _ in range(R)]
        invalid = set([(3, 0), (3, 2)])
        for r, c in invalid:
            dp[r][c] = 0
        dirs = [
            (2, 1), (-2, 1), (2, -1), (-2, -1),
            (1, 2), (-1, 2), (1, -2), (-1, -2)
        ]
        for _ in range(n - 1):
            dp2 = [[0] * C for _ in range(R)]
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    if (r, c) in invalid:
                        continue
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if (nr, nc) in invalid:
                            continue
                        if 0 <= nr < R and 0 <= nc < C:
                            dp2[nr][nc] += val
            dp = dp2

        return sum(map(sum, dp)) % (pow(10, 9) + 7)
