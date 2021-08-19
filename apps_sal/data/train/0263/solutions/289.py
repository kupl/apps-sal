class Solution:

    def knightDialer(self, n: int) -> int:
        mod = 10 ** 9 + 7
        reachFrom = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        dp = [[1] * 10 for _ in range(2)]
        for i in range(1, n):
            for j in range(10):
                dp[i % 2][j] = 0
                for src in reachFrom[j]:
                    dp[i % 2][j] += dp[(i - 1) % 2][src]
        return sum(dp[(n - 1) % 2]) % mod
