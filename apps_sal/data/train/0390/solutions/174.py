"""
    1 - Alice
    2 - Bob
    3 - Alice
    4 - Alice
    5 - [1 (Bob), 4(Bob)]
    6 - [1 (Alice), 4(Bob)] 
    7 - [1, 4]
    n - Alice
    n+1 -
"""


class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        if n == 1:
            return True
        dp = [False] * (n + 1)
        squares = set()
        for i in range(1, n // 2 + 1):
            square = i * i
            if square <= n:
                squares.add(square)
                dp[square] = True
        for i in range(1, n + 1):
            if i not in squares:
                possible = [not dp[i - square] for square in squares if square < i]
                dp[i] = any(possible)
        return dp[-1]
