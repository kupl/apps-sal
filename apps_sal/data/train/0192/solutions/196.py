class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        out = 0
        count = 0
        hi = len(piles) - 1
        lo = 0
        while count < len(piles):
            if count % 3 == 0:
                hi -= 1
            elif count % 3 == 1:
                out += piles[hi]
                hi -= 1
            else:
                lo += 1
            count += 1
        return out
