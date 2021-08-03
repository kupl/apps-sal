class Solution:
    @lru_cache(None)
    def winnerSquareGame(self, n: int) -> bool:
        if n == 1:
            return True
        s = 1
        while s * s <= n:
            flag = self.winnerSquareGame(n - s * s)
            if flag == False:
                return True
            s += 1
        return False
