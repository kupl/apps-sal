class Solution:

    def knightDialer(self, n: int) -> int:
        neighbors = {1: (6, 8), 2: (7, 9), 3: (4, 8), 4: (3, 9, 0), 5: tuple(), 6: (1, 7, 0), 7: (2, 6), 8: (1, 3), 9: (2, 4), 0: (4, 6)}
        dp = [[0 for _ in range(10)] for _ in range(n + 1)]
        for r in range(n + 1):
            for c in range(10):
                if r == 0:
                    dp[r][c] = 0
                elif r == 1:
                    dp[r][c] = 1
                else:
                    for ne in neighbors[c]:
                        dp[r][c] += dp[r - 1][ne]
        return sum(dp[-1]) % (10 ** 9 + 7)
