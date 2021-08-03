class Solution:
    def shipWithinDays(self, weights, D: int) -> int:
        if not weights or not D:
            return 0

        lo, hi = max(weights), sum(weights)
        ans = 0
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            res = self.validate(weights, D, mid)
            if res == 1:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans

    def validate(self, weights, D, capacity):
        count = 0
        w = 0
        D -= 1
        while w < len(weights):
            if count + weights[w] <= capacity:
                count += weights[w]
            else:
                count = weights[w]
                D -= 1
                if D < 0:
                    break
            w += 1
        if w == len(weights):
            return 1
        else:
            return -1
