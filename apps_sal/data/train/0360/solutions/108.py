class Solution:
    def possible(self, capacity):
        ret = 0
        cur = 0
        for w in self.weights:
            if w > capacity:
                return False
            if cur + w <= capacity:
                cur += w
            else:
                ret += 1
                cur = w
        if w > 0:
            ret += 1
        return ret <= self.D

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        self.weights = weights
        self.D = D

        lo, hi = 1, 0x3f3f3f3f
        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)

            if self.possible(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        if self.possible(lo):
            return lo
        return lo + 1
