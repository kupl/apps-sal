class Solution:

    def winnerSquareGame(self, n: int) -> bool:

        @lru_cache(None)
        def dp(n, people):
            for i in range(floor(math.sqrt(n)), 0, -1):
                if i * i <= n:
                    result = dp(n - i * i, 0 if people is 1 else 1)
                    if people == 0:
                        if result:
                            return result
                    elif not result:
                        return result
            if people == 0:
                return False
            else:
                return True
        return dp(n, 0)
