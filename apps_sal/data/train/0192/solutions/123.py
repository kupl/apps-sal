class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        count = 0
        piles.sort()

        while len(piles) > 0:

            piles.pop(-1)

            count += piles[-1]
            piles.pop(-1)

            piles.pop(0)

        return count
