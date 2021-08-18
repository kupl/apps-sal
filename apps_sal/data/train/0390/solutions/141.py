class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [0] * (n + 1)
        squares = []
        i = 1
        nxt_sqrt = 1
        nxt = 1
        for i in range(1, n + 1):
            if i == nxt:
                dp[i] = 1
                squares.append(nxt)
                nxt_sqrt += 1
                nxt = nxt_sqrt ** 2
            else:
                dp[i] = max(-dp[i - s] for s in squares)
        return dp[n] == 1
