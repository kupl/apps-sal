class Solution:
    def knightDialer(self, n: int) -> int:

        def knightPos(i, j):
            # left top bot
            lt = (i + 2, j - 1)
            lb = (i - 2, j - 1)
            # right top bot
            rt = (i + 2, j + 1)
            rb = (i - 2, j + 1)
            # top left right
            tl = (i + 1, j - 2)
            tr = (i + 1, j + 2)
            # bot left right
            bl = (i - 1, j - 2)
            br = (i - 1, j + 2)

            return (lt, lb, rt, rb, tl, tr, bl, br)

        dp = [[1] * 3 for _ in range(4)]
        dp[3][0] = dp[3][2] = 0
        mod = (10**9) + 7

        for k in range(1, n):
            tmp = [[0] * 3 for _ in range(4)]
            for i in range(4):
                for j in range(3):
                    if (i == 3 and j == 0) or (i == 3 and j == 2):
                        continue
                    for x, y in knightPos(i, j):
                        if 0 <= x <= 3 and 0 <= y <= 2:
                            tmp[i][j] += dp[x][y]
            dp = tmp

        return sum([sum(i) for i in dp]) % mod
