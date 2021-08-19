class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        (left, right) = (max(weights), sum(weights))

        def condition(m):
            days = 0
            cap = m
            n = len(weights)
            i = 0
            while i < n:
                w = weights[i]
                if m - w >= 0:
                    m -= w
                    i += 1
                else:
                    days += 1
                    m = cap - w
                    i += 1
                if days > D:
                    return False
            days += 1
            if days > D:
                return False
            return True
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left
