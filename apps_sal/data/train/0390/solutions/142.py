class Solution:
    # dp(i): remain i piles
    def winnerSquareGame(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        squares = [i**2 for i in range(1, int(sqrt(n)) + 1)]

        @lru_cache(None)
        def dp(i):
            nonlocal squares
            canWin = False
            for sq in squares:
                if i < sq:
                    break
                if i == sq:
                    return True
                canWin = canWin or not dp(i - sq)
            return canWin
        return dp(n)
