class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        
        lo, hi = float('inf'), -float('inf')
        for day in bloomDay:
            lo = min(lo, day)
            hi = max(hi, day)
        
        def check(d): # check if D days is good enough for m bouquets of k flowers
            cnt, start = 0, -1
            for i, val in enumerate(bloomDay):
                if val <= d and i - start >= k:
                    cnt += 1
                    start = i
                elif val > d:
                    start = i
            return cnt >= m
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
