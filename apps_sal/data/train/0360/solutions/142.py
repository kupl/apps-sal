class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:

        def isPossible(capacity):
            day = 1
            w = 0
            for wt in weights:
                w += wt
                if w > capacity:
                    day += 1
                    w = wt
            return day

        start, end = max(max(weights), sum(weights) // D), sum(weights)

        while start < end:
            mid = start + (end - start) // 2
            days = isPossible(mid)
            if days <= D:
                end = mid
            elif days > D:
                start = mid + 1

        return start
