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

    def stoneGame(self, piles: List[int]) -> bool:
        if not piles:
            return False
        n = len(piles)
        nums = piles
        dp = [[[None, None] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i][0] = -nums[i]
            dp[i][i][1] = nums[i]
        for l in range(1, n):
            for i in range(n - l):
                j = i + l
                dp[i][j][0] = min(-nums[i] + dp[i + 1][j][1], -nums[j] + dp[i][j - 1][1])
                dp[i][j][1] = max(nums[i] + dp[i + 1][j][0], nums[j] + dp[i][j - 1][0])

        return dp[0][n - 1][1] > 0
