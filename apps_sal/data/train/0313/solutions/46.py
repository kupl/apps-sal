class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        lo = min(bloomDay)
        hi = max(bloomDay)
        while lo < hi:
            mid = lo + (hi-lo)//2
            pos_b = 0
            cur_b = 0
            for f in bloomDay:
                if f <= mid:
                    cur_b += 1
                else:
                    cur_b = 0
                if cur_b == k:
                    pos_b += 1
                    cur_b = 0
            if pos_b >= m:
                hi = mid
            else:
                lo = mid+1
        return lo
