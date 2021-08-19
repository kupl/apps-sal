class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        start = len(piles) - 1
        end = 0
        total = 0
        while end < start:
            total += piles[start - 1]
            start -= 2
            end += 1
        return total
