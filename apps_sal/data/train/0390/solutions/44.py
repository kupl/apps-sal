class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        wins = [False for i in range(n + 1)]
        wins[1] = True
        for i in range(2, n + 1):
            j = 1
            while i - j * j >= 0:
                if wins[i - j * j] == False:
                    wins[i] = True
                    break
                j += 1
        return wins[n]
