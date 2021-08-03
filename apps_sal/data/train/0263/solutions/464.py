class Solution:
    def knightDialer(self, N: int) -> int:
        d = {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 1)}
        dirs = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (1, 2), (-1, -2), (1, -2)]
        m = 10**9 + 7
        dp = {}
        for x in d:
            dp[x] = [0] * (N + 1)
            dp[x][1] = 1

        for n in range(2, N + 1):
            for r, c in d:
                for z in dirs:
                    rz, cz = r + z[0], c + z[1]
                    if (rz, cz) in d:
                        dp[(r, c)][n] = (dp[(r, c)][n] + dp[(rz, cz)][n - 1]) % m
        return sum(x[N] for x in dp.values()) % m
