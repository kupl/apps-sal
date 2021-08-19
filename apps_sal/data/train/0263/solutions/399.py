class Solution:

    def getAccessible(self, key):
        switch = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        return switch.setdefault(key, [])

    def knightDialer(self, n: int) -> int:
        dp = [[0] * 10 for _ in range(n)]
        dp[0] = [1] * 10
        for r in range(1, len(dp)):
            for c in range(len(dp[0])):
                neighbors = self.getAccessible(c)
                for n in neighbors:
                    dp[r][c] = dp[r - 1][n] + dp[r][c] % (10 ** 9 + 7)
        return sum(dp[-1]) % (10 ** 9 + 7)
