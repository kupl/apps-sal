class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res = 0
        while piles:
            piles.pop()
            res += piles.pop()
            piles.pop(0)
        return res
