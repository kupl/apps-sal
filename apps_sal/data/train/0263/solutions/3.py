class Solution:

    def knightDialer(self, n: int) -> int:
        possibleMoves = [[4, 6], [6, 8], [9, 7], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        dp = [1] * 10
        upper = 10 ** 9 + 7
        for i in range(n - 1):
            dp2 = [0] * 10
            for j in range(10):
                for adj in possibleMoves[j]:
                    dp2[adj] = (dp2[adj] + dp[j]) % upper
            dp = dp2
        return sum(dp) % upper
