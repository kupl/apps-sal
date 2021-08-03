class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [[1] * 10 for _ in range(n + 1)]

        d = {
            0: (4, 6),
            1: (6, 8),
            2: (7, 9),
            3: (8, 4),
            4: (3, 9, 0),
            5: (),
            6: (1, 7, 0),
            7: (6, 2),
            8: (1, 3),
            9: (2, 4)
        }

        for i in range(2, n + 1):
            for j in range(0, 10):
                dp[i][j] = 0
                for k in d[j]:
                    dp[i][j] += dp[i - 1][k]

        return sum(dp[n]) % (10**9 + 7)
