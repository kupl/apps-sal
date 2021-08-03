class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def time_needed(time):
            return sum(p // time + (1 if p % time else 0) for p in piles)

        lower = max(1, sum(piles) // H)
        upper = max(piles)

        while lower < upper:
            time_lower = time_needed(lower)
            if time_lower <= H:
                return lower

            lower += 1
            mid = (lower + upper) // 2
            time_mid = time_needed(mid)
            if time_mid <= H:
                upper = mid
            else:
                lower = mid + 1

        return lower
