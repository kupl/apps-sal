class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        (l, r) = (max(weights), sum(weights))
        while l <= r:
            m = l + (r - l) // 2
            if self.loadBalancer(weights, m) > D:
                l = m + 1
            elif self.loadBalancer(weights, m) <= D:
                r = m - 1
        return l

    def loadBalancer(self, weights, target):
        (c, sum_) = (1, 0)
        for i in weights:
            if sum_ + i > target:
                c += 1
                sum_ = 0
            sum_ += i
        return c
