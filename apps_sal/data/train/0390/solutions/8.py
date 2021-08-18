import math


class Solution:
    squares = []
    dp = {}

    def util(self, n):
        if n == 0:
            return False
        if n in self.dp:
            return self.dp[n]

        for i in range(1, int(math.sqrt(n)) + 1):
            if not self.util(n - self.squares[i]):
                self.dp[n] = True
                return True
        self.dp[n] = False
        return False

    def winnerSquareGame(self, n: int) -> bool:
        self.squares = []
        for i in range(int(math.sqrt(n)) + 1):
            self.squares.append(i * i)
        return self.util(n)
