class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        t = 0
        while piles:
            piles.pop()
            t += piles.pop()
            del piles[0]
        return t
