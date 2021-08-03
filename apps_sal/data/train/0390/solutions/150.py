class Solution:
    @lru_cache(None)
    def winnerSquareGame(self, n: int) -> bool:
        if n == 1:
            return True
        sqrt = math.floor(math.sqrt(n))
        if sqrt * sqrt == n:
            return True
        for num in range(1, sqrt + 1):
            if not self.winnerSquareGame(n - num**2):
                return True
        return False
