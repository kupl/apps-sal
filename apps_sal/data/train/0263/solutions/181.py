class Solution:

    def knightDialer(self, n: int) -> int:
        dp = [[1] * 10 for _ in range(n)]
        moves = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        for i in range(1, n):
            for j in range(10):
                count = 0
                for digit in moves[j]:
                    count += dp[i - 1][digit]
                dp[i][j] = count
        return sum(dp[-1]) % (10 ** 9 + 7)
