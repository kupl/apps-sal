class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        wins = [False] * (n + 1)
        for i in range(1, n + 1):
            j = 1
            canWin = False
            while j * j <= i and not canWin:
                canWin = not wins[i - j * j]
                j += 1
            wins[i] = canWin

        return wins[n]
