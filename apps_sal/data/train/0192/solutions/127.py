class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        sums = 0
        while piles:
            (m1, m2) = (piles.pop(), piles.pop())
            m3 = piles.pop(0)
            sums += m2
        return sums
