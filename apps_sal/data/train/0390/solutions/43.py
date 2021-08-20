class Solution:

    def winnerSquareGame(self, n: int) -> bool:

        @lru_cache(None)
        def dfs(idx):
            if idx == 0:
                return False
            for i in range(1, int(math.sqrt(idx)) + 1):
                if dfs(idx - i * i) == False:
                    return True
            return False
        return dfs(n)
