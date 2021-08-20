class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles, reverse=True)
        num2 = len(piles) // 3
        piles = piles[:-num2]
        print(piles)
        return sum((el for (i, el) in enumerate(piles) if i % 2 == 1))
