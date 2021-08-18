class Solution:

    def __init__(self):
        self.helper = {(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)}

    def dynamic(self, r, c, dp):

        curr = 0
        for s in self.helper:
            x, y = r + s[0], c + s[1]

            if 0 <= x < 4 and 0 <= y < 3 and ((x, y) != (3, 0) or (x, y) != (3, 2)):
                curr += dp[x][y]
        return curr

    def knightDialer(self, n: int) -> int:

        dp = [[1] * 3 for _ in range(4)]

        dp[3][0] = dp[3][2] = 0

        for i in range(n - 1):
            dp2 = [[0] * 3 for _ in range(4)]

            for r in range(4):
                for c in range(3):
                    if (r, c) == (3, 0) or (r, c) == (3, 2):
                        continue

                    dp2[r][c] = self.dynamic(r, c, dp)
            dp = dp2[:]
        return sum([dp[i][j] for i in range(4) for j in range(3)]) % (10**9 + 7)
