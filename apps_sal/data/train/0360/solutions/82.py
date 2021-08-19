class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        self.weight = weights
        self.D = D
        hi = sum(weights)
        lo = 1
        while hi != lo:
            mid = (hi + lo) // 2
            if self.if_fit(mid):
                hi = mid
            else:
                lo = mid + 1
        return hi

    def if_fit(self, cap):
        d = 1
        count = 0
        for val in self.weight:
            if val > cap:
                return False
            if val + count <= cap:
                count += val
            else:
                count = val
                d += 1
                if d > self.D:
                    return False
        return True
