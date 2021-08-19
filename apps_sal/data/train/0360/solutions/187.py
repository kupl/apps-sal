class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:

        def __can(capacity):
            days = 0
            partial_sum = 0
            for i in range(len(weights)):
                if partial_sum + weights[i] > capacity:
                    partial_sum = 0
                    days += 1
                partial_sum += weights[i]
            days += 1
            return days <= D
        (lo, hi) = (max(weights), sum(weights))
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if __can(mid) == True:
                hi = mid
            else:
                lo = mid
        return lo if __can(lo) == True else hi
