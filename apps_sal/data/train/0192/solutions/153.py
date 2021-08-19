class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        out = 0
        piles.sort()
        while len(piles) >= 3:
            piles.pop()
            out += piles.pop()
            piles.pop(0)
        return out
