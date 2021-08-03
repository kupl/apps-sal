class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def possible(K):
            if K < max(weights):
                return False
            day = 1
            temp = K
            for we in weights:
                if temp < we:
                    temp = K - we
                    day += 1
                else:
                    temp -= we

            return not (day > D)
        lo, hi = max(weights), sum(weights)

        while lo < hi:

            mi = (lo + hi) // 2
            if not possible(mi):
                lo = mi + 1
            else:
                hi = mi

        return lo
