class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:

        def canShip(maxCapacity):
            days = 0
            cur = 0
            for w in weights:
                if cur + w <= maxCapacity:
                    cur += w
                else:
                    cur = w
                    days += 1
            days += 1
            return days <= D
        l = max(weights)
        r = sum(weights)
        while l < r:
            mid = (l + r) // 2
            if canShip(mid):
                r = mid
            else:
                l = mid + 1
        return l
