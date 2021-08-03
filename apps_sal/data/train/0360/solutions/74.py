class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def possible(cap):
            s = 0
            ship = 0
            i = 0
            while i < len(weights):
                s = s + weights[i]
                if s > cap:
                    ship = ship + 1
                    s = 0
                elif s < cap:
                    i = i + 1
                else:
                    ship = ship + 1
                    s = 0
                    i = i + 1
            if s == 0:
                return ship <= D
            else:
                return (ship + 1) <= D
        lo = max(weights)
        hi = sum(weights)
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if possible(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
