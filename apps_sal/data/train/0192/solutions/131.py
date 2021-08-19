class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        t = 0
        piles.sort()
        for i in range(n // 3 - 1):
            t += piles[-2]
            piles.pop(0)
            piles.pop(-1)
            piles.pop(-2)
        t += piles[-2]
        return t
