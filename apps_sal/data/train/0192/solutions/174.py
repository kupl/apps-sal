class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res = 0
        while piles:
            a = piles.pop()
            b = piles.pop()
            c = piles.pop(0)
            res += b
        return res
