class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        @lru_cache(maxsize=None)
        def dfs(remain):
            sqrt_root = int(remain**0.5)
            if sqrt_root ** 2 == remain:
                return True

            for i in range(1, sqrt_root + 1):
                if not dfs(remain - i * i):
                    return True

            return False

        return dfs(n)
