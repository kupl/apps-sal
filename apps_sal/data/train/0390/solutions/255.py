from functools import lru_cache


class Solution:

    def winnerSquareGame(self, n: int) -> bool:

        @lru_cache(None)
        def dp(i):
            sq = int(math.sqrt(i))
            if sq ** 2 == i:
                return True
            ans = False
            for m in [n ** 2 for n in range(1, sq + 1)][::-1]:
                ans = ans or not dp(i - m)
                if ans:
                    return True
            return ans
        return dp(n)
