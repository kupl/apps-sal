class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        lo = max(weights)
        hi = sum(weights)
        res = hi
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            days = 0
            curr_weight = 0
            for i in range(len(weights)):
                if curr_weight + weights[i] > mid:
                    days += 1
                    curr_weight = weights[i]
                else:
                    curr_weight += weights[i]
            days += 1
            if days <= D:
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return res
