class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        count = 0
        while piles:
            piles.pop()
            count += piles.pop()
            piles.pop(0)
        return count
