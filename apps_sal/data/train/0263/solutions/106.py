class Solution:
    def knightDialer(self, n: int) -> int:
        positions = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [0, 3, 9],
            [],
            [0, 1, 7],
            [2, 6],
            [1, 3],
            [2, 4]
        ]
        
        dp = [[0 for i in range(n + 1)] for i in range(10)]
        
        for i in range(10):
            dp[i][1] = 1
        
        for j in range(2, n + 1):
            for i in range(10):
                for pos in positions[i]:
                    dp[i][j] = (dp[i][j] + dp[pos][j - 1]) % 1000000007
        
        result = 0
        
        for i in range(10):
            result = (result + dp[i][n]) % 1000000007
        
        return result
