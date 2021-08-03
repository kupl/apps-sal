class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        @lru_cache(maxsize=None)
        def dfs(remain):

            sqrts = int(sqrt(remain))
            if sqrts ** 2 == remain:
                return True

            for i in range(1, sqrts + 1):

                if not dfs(remain - i * i):
                    return True
            return False

        return dfs(n)
