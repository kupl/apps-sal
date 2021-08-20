class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:

        def canship(cap):
            d = 1
            s = 0
            for w in weights:
                if s + w <= cap:
                    s += w
                else:
                    d += 1
                    s = w
                if d > D:
                    return False
            return True
        M = max(weights)
        if D == len(weights):
            return M
        (lo, hi) = (M - 1, sum(weights))
        while hi - lo > 1:
            h = (hi + lo) // 2
            if canship(h):
                hi = h
            else:
                lo = h
        return hi
