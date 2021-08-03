class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:

        def fun(t):
            s = 0
            d = 0
            for i in range(n):
                s = s + weights[i]
                if s > t:
                    d = d + 1
                    s = weights[i]
            return d

        n = len(weights)
        lo, hi = max(weights), sum(weights)
        while(lo <= hi):
            c = lo + (hi - lo) // 2
            if fun(c) < D:
                hi = c - 1
            else:
                lo = c + 1
        return lo
