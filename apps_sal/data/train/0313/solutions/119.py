class Solution:

    def minDays(self, blooms: List[int], m: int, k: int) -> int:
        if m * k > len(blooms):
            return -1
        (lo, hi) = (0, max(blooms))

        def is_possible(today):
            streak = bouquets = 0
            for day in blooms:
                if day <= today:
                    streak += 1
                    if streak == k:
                        bouquets += 1
                        streak = 0
                else:
                    streak = 0
            return bouquets >= m
        while lo < hi:
            mid = (lo + hi) // 2
            if not is_possible(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo
