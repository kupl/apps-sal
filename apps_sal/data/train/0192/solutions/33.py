class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        (first, last) = (0, len(piles) - 1)
        total = 0
        while first < last:
            total += piles[last - 1]
            first += 1
            last -= 2
        return total
