class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[-1 for _ in range(n)] for _ in range(n)]

        def score_helper(l, r):
            if l > r:
                return 0
            if l == r:
                return piles[l]
            if dp[l][r] != -1:
                return dp[l][r]
            dp[l][r] = max(piles[l] - dp[l + 1][r], piles[r] - dp[l][r - 1])
            return score_helper(0, n - 1)

        return score_helper(0, n - 1) >= 0
