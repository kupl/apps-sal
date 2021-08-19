class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res = 0
        while piles:
            first = piles.pop(-1)
            second = piles.pop(-1)
            third = piles.pop(0)
            res += second
        return res
