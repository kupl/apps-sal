class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:

        def good(cap):
            i, tmp, ans = 0, 0, 1
            while i < len(a):
                if tmp + a[i] <= cap:
                    tmp += a[i]
                else:
                    ans += 1
                    tmp = a[i]
                i += 1
            return ans <= D

        a = weights
        lo, hi = max(a), sum(a)
        while lo < hi:
            mid = (lo + hi) // 2
            if good(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
