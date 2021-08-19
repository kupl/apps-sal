class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        high = 0
        low = 0
        for weight in weights:
            high += weight
            low = max(low, weight)

        # Search over the possible solutions of [max value, sum of weights]
        while (low < high):
            mid = (high + low) // 2

            days = 1
            cur_weight = 0
            for weight in weights:
                if cur_weight + weight > mid:
                    cur_weight = 0
                    days += 1
                cur_weight += weight

            # Did it in too many days, need higher capacity
            if days > D:
                low = mid + 1
            # Did it in too few days, need lower capacity
            else:
                high = mid

        return low
