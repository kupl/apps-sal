class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [None] * (n + 1)
        squares = []
        for i in range(1, n + 1):
            if i ** 2 > n:
                break
            squares.append(i**2)
            dp[i**2] = True
        for i in range(1, n + 1):
            if dp[i] is not None:
                continue
            cur = True
            for s in squares:
                if s > i:
                    break
                cur = cur and dp[i - s]
            dp[i] = not cur
        return dp[n]
