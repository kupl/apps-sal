class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        def backtracking(i, j):
            if i == j:
                return piles[i]
            if not (i + 1, j) in dp:
                dp[i + 1, j] = backtracking(i + 1, j)
            res = piles[i] - dp[i + 1, j]
            if not (i, j - 1) in dp:
                dp[i, j - 1] = backtracking(i, j - 1)
            res = max(res, piles[j] - dp[i, j - 1])
            return res
        return backtracking(0, len(piles) - 1) > 0
