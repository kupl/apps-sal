class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def valid(interval, m):
            last = -interval
            for p in position:
                if p - last >= interval:
                    m -= 1
                    last = p
            return True if m <= 0 else False
        # binary search interval: return the maxiumal interval
        lo, hi = 1, max(position) // (m - 1)  # the interval cannot be than the ideal condition
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if valid(mid, m):  # the correct value can be bigger
                lo = mid + 1  # [min,lo-1] is valid all the time
            else:
                hi = mid - 1  # [hi+1,max] is not valid all the time
        # lo=hi+1; [min,lo-1] is valid, [lo,max] is not valid
        return hi
