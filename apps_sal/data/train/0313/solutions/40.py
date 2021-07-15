class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = max(bloomDay)
        if m*k > len(bloomDay):
            return -1
        
        l, r = 1, n
        while l <= r:
            mid = (l+r)//2
            count, rec = 0, 0
            
            for i in range(len(bloomDay)):
                if bloomDay[i] <= mid:
                    count += 1
                    if count >= k:
                        rec += 1
                        count = 0
                    if rec >= m:
                        break
                else:
                    count = 0
            
            if rec < m: #need more bouquets, increase the mid makes it easy to collect flowers
                l = mid+1
            else:
                r = mid-1
        
        return l

