class Solution:
    def knightDialer(self, n: int) -> int:
        moves = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        
        # dp [i][j] = distinct phone numbers reachable of length j if you are at number i
        # 0 <= i <= 9
        # 0 <= j <= n
        
        dp = [[0 for j in range(n + 1)] for i in range(10)]
        
        for j in range(n + 1):
            for i in range(10):
                if (j <= 1):
                    dp[i][j] = 1
                else:
                    dp[i][j] = sum([dp[possibleMove][j - 1] for possibleMove in moves[i]])

        return sum([dp[i][n] for i in range(10)]) % (10 ** 9 + 7)

