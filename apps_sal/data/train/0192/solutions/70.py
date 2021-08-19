class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        sorted_piles = sorted(piles)
        piles_len = len(sorted_piles)
        start = int(piles_len / 3)
        counter = 0
        for x in range(start, piles_len, 2):
            counter += sorted_piles[x]
        return counter
