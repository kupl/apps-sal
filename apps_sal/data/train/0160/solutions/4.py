class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(None)
        def dfs(i, j, isAlex):
            if j < i:
                return 0
            elif i == j:
                return piles[i] if isAlex else -piles[i]
            if isAlex:
                return max(piles[i] + dfs(i + 1, j, not isAlex), piles[j] + dfs(i, j - 1, not isAlex))
            else:
                return min(-piles[i] + dfs(i + 1, j, not isAlex), -piles[j] + dfs(i, j - 1, not isAlex))

        if not piles:
            return False
        n = len(piles)

        return dfs(0, n - 1, True) > 0
