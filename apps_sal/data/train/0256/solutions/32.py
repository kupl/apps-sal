class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        def time_needed(K):
            return sum((p // K + (1 if p % K else 0) for p in piles))
        lower = max(1, sum(piles) // H)
        upper = max(piles)
        while lower < upper:
            if time_needed(lower) <= H:
                return lower
            lower += 1
            mid = (lower + upper) // 2
            if time_needed(mid) <= H:
                upper = mid
            else:
                lower = mid + 1
        return lower
