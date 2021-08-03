class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:

        def days_required(t):
            running_sum = 0
            days = 0
            for i in range(n):
                running_sum += weights[i]
                if running_sum > t:
                    days += 1
                    running_sum = weights[i]
            return days

        n = len(weights)
        lo, hi = max(weights), sum(weights)
        while(lo <= hi):
            capacity = lo + (hi - lo) // 2
            if days_required(capacity) < D:
                hi = capacity - 1
            else:
                lo = capacity + 1
        return lo
