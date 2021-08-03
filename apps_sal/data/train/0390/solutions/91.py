class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(None)
        def win(amt):
            x = int(math.sqrt(amt))
            for i in range(x, 0, -1):
                if not win(amt - i * i):
                    return True
            return False
        return win(n)
