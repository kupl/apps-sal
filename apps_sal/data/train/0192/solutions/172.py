class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        complete_sorted = sorted(piles)
        result = 0
        while complete_sorted:
            complete_sorted.pop()
            result += complete_sorted.pop()
            complete_sorted.pop(0)
        return result
