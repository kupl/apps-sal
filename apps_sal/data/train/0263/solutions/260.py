class Solution:

    def knightDialer(self, n: int) -> int:
        moves = [[] for x in range(10)]
        moves[0] = [4, 6]
        moves[1] = [6, 8]
        moves[2] = [7, 9]
        moves[3] = [4, 8]
        moves[4] = [3, 9, 0]
        moves[5] = []
        moves[6] = [0, 1, 7]
        moves[7] = [2, 6]
        moves[8] = [1, 3]
        moves[9] = [2, 4]
        dp = {}

        def dialer(start, n):
            if (start, n) in dp:
                return dp[start, n]
            if n == 1:
                dp[start, n] = 1
                return 1
            xmoves = 0
            for move in moves[start]:
                xmoves += dialer(move, n - 1)
            xmoves %= 10 ** 9 + 7
            dp[start, n] = xmoves
            return xmoves
        xmoves = 0
        for i in range(10):
            xmoves += dialer(i, n)
        return xmoves % (10 ** 9 + 7)
