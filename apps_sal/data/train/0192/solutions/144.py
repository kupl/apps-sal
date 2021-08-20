class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        mine = 0
        while piles:
            piles.pop(-1)
            mine += piles.pop(-1)
            piles.pop(0)
        return mine
