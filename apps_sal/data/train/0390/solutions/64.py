class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        losers = {0}
        for x in range(1, n + 1):
            flag = True
            for y in range(1, int(x**0.5) + 1):
                if (x - y**2) in losers:
                    flag = False
                    break
            if flag:  # Its a loser position because you cant send the next player to a loser position
                losers.add(x)
        return False if n in losers else True
