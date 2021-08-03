class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        def backtracking(i, j):
            if i == j:
                return piles[i]
            if not (i, j) in dp:
                dp[(i, j)] = max(piles[i] - backtracking(i + 1, j), piles[j] - backtracking(i, j - 1))
            return dp[(i, j)]

        return backtracking(0, len(piles) - 1) > 0
