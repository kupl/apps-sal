class Solution:
    def knightDialer(self, N: int) -> int:
        possible_moves = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [3, 9, 0],
            [],
            [1, 7, 0],
            [2, 6],
            [1, 3],
            [2, 4]
        ]
        
        dp = [1 for _ in range(10)]
        for _ in range(1, N):
            dp1 = [0 for _ in range(10)]
            for i in range(10):
                for m in possible_moves[i]:
                    dp1[i] += dp[m]
            dp = dp1
        
        return sum(dp) % (pow(10, 9) + 7)
