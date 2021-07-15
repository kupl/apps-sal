class Solution:
    def knightDialer(self, n: int) -> int:
        moves = [
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
        dp = [1] * 10
        for _ in range(n - 1):
            prevDp = copy.copy(dp)
            for i in range(10):
                dp[i] = sum([prevDp[move] for move in moves[i]])
        return sum(dp) % (10**9 + 7)
            
            

