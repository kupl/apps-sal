class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        a = 0
        y = 0
        b = 0
        while piles != []:
            a = a + piles.pop()
            y = y + piles.pop()
            b = b + piles.pop(0)
        return y
