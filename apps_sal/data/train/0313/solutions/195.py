class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        min_day = min(bloomDay)
        max_day = max(bloomDay)
        lbd = len(bloomDay)
        
        if lbd < m*k:
            return -1
        
        while min_day < max_day:
            mid = (min_day + max_day - 1)//2
            
            nk, nm = 0, 0
            for i in range(lbd):
                
                if bloomDay[i] <= mid:
                    nk += 1
                else:
                    nk = 0
                if nk >= k:
                    nm += 1
                    nk = 0
            if nm < m:
                min_day = mid + 1
            else:
                max_day = mid
            
        return min_day
                    
            
            
            
        
        
        

