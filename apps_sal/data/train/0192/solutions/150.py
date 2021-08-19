class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        mine = []
        while piles:
            _ = piles.pop()
            _ = piles.pop(0)
            mine.append(piles.pop())
        return sum(mine)
