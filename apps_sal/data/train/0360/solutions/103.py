class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        (start, end) = (max(weights), sum(weights) + 1)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self._can_ship(weights, mid, D):
                end = mid
            else:
                start = mid
        return start if self._can_ship(weights, start, D) else end

    def _can_ship(self, weights, capacity, D):
        days_needed = 0
        i = 0
        while i < len(weights):
            curr_w = 0
            while i < len(weights) and curr_w + weights[i] <= capacity:
                curr_w += weights[i]
                i += 1
            days_needed += 1
        return days_needed <= D
