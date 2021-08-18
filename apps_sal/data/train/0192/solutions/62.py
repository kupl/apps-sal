class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i = 0
        start = 0
        end = len(piles) - 2
        res = 0
        while i < len(piles) // 3:
            res += piles[end]
            end -= 2
            i += 1
        return res
