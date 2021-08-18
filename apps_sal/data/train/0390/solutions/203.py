class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(None)
        def dp(n, people):
            for i in range(1, 400):
                if i * i <= n:
                    result = dp(n - i * i, 0 if people is 1 else 1)
                    if people == 0:
                        if result:
                            return result
                    else:
                        if not result:
                            return result
                else:
                    break
            if people == 0:
                return False
            else:
                return True
        return dp(n, 0)
