class Solution:

    def check(self, weights: List[int], D: int, cap: int) -> bool:
        load = 1
        total = 0
        for i in range(len(weights)):
            total += weights[i]
            if i != len(weights) - 1:
                if total + weights[i + 1] > cap:
                    total = 0
                    load += 1
                    if load > D:
                        return False
        if load <= D:
            return True

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        lo = max(weights)
        hi = sum(weights)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.check(weights, D, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
