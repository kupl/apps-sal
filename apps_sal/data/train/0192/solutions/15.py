class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        rounds = len(piles) // 3
        score = 0

        piles.sort()
        for x in range(len(piles) - 2, rounds - 1, -2):
            score += piles[x]

        return score
