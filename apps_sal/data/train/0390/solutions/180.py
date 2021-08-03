class Solution:
    def __init__(self):
        self.isGood = {}

    def winnerSquareGame(self, n: int) -> bool:
        if n <= 0:
            return False

        if n in self.isGood:
            return self.isGood[n]

        self.isGood[n] = False
        i = 1
        while i * i <= n:
            if not self.winnerSquareGame(n - i * i):
                self.isGood[n] = True
                return True
            i += 1

        return self.isGood[n]
