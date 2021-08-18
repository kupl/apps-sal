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
        lo, hi = 1, max(position) // (m - 1)
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if valid(mid, m):
                lo = mid + 1
            else:
                hi = mid - 1
        return hi
