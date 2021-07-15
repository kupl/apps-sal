class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        res = 0
        piles.sort()
        while len(piles) > 0:
            piles.pop(0)
            piles.pop(-1)
            res += piles.pop(-1)
        return res
