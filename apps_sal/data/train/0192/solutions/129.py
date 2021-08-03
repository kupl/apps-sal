class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        result = 0
        while len(piles) > 0:
            piles.pop()
            result += piles.pop()
            piles.pop(len(piles) // 3)
        return result
