class Solution:

    def winnerSquareGame(self, n: int) -> bool:

        def is_square(n):
            root = math.sqrt(i)
            return root == int(root)
        dp = [False] * (n + 1)
        squares = []
        for i in range(1, n + 1):
            if is_square(i):
                squares.append(i)
            dp[i] = any((not dp[i - square] for square in squares))
        return dp[-1]
