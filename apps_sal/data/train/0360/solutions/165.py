class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        high = 0
        low = 0
        for weight in weights:
            high += weight
            low = max(low, weight)
        while low < high:
            mid = (high + low) // 2
            days = 1
            cur_weight = 0
            for weight in weights:
                if cur_weight + weight > mid:
                    cur_weight = 0
                    days += 1
                cur_weight += weight
            if days > D:
                low = mid + 1
            else:
                high = mid
        return low
