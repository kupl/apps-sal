class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        lower = 1
        upper = max(piles)
        while lower < upper:
            mid = (lower + upper) // 2
            if sum((p // mid + 1 if p % mid else p // mid for p in piles)) > H:
                lower = mid + 1
            else:
                upper = mid
        return upper
