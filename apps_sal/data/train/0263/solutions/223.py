class Solution:
    def knightDialer(self, n: int) -> int:
        # dp[i][move] = [dp[neighbor][move - 1]for neighbor in neighbors]
        neighbors = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        if n == 0:
            return 0
        dp = [[1 for i in range(n)] for i in range(10)]
        for move in range(1, n):
            for num in range(10):
                dp[num][move] = sum([dp[neighbor][move - 1] for neighbor in neighbors[num]]) % 1000000007
        return sum([dp[num][n - 1] for num in range(10)]) % 1000000007
