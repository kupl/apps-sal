class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        start, end = max(weights), sum(weights)
        while start + 1 < end:
            mid = (start + end) // 2
            days = self.get_days(weights, mid)
            if days > D:
                start = mid + 1
            elif days <= D:
                end = mid
        if self.get_days(weights, start) <= D:
            return start
        else:
            return end

    def get_days(self, weights, cap):
        tot = 0
        res = 1
        i = 0
        while i < len(weights):
            tot += weights[i]
            if tot > cap:
                res += 1
                tot = 0
            else:
                i += 1
        return res
