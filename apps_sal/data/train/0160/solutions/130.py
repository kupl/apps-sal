class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        memo = piles[:]
        for l in range(2, n + 1):
            for i in range(n + 1 - l):
                memo[i] = max(piles[i] - memo[i + 1], piles[i + l - 1] - memo[i])
        return memo[0]
