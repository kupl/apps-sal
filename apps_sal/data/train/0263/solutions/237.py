class Solution:
    def knightDialer(self, n: int) -> int:
        mod = pow(10, 9) + 7
        maps = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
        }
        
        dp = [[0] * n for _ in range(10)]
        for i in range(10):
            dp[i][0] = 1
            
        for i in range(1, n):
            for digit in range(10):
                dp[digit][i] = sum(dp[j][i-1] for j in maps[digit])
                
        return sum(dp[digit][-1] for digit in range(10)) % mod

