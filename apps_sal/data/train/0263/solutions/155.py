class Solution:

    def knightDialer(self, n: int) -> int:
        dp = [[0 for _ in range(10)] for _ in range(n + 1)]
        prevs = {0: [4, 6], 1: [8, 6], 2: [7, 9], 3: [8, 4], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [6, 2], 8: [1, 3], 9: [4, 2]}
        for i in range(10):
            dp[1][i] = 1
        for i in range(2, n + 1):
            for j in range(10):
                for prev in prevs[j]:
                    dp[i][j] += dp[i - 1][prev]
        return sum(dp[-1]) % 1000000007
