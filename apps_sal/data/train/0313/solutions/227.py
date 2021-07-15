class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        if len(bloomDay) < m * k:
            return -1
        
        b = min(bloomDay)
        e = max(bloomDay)
        
        def check_day(day):
            flowers = 0
            bouquets = 0
            for d in bloomDay:
                if d > day:
                    flowers = 0
                else:
                    flowers += 1
                    if flowers >= k:
                        bouquets += 1
                        flowers = 0
                        if bouquets >= m:
                            return True
            return False
        
        while e>=b:
            mid = (b+e)//2
            
            if check_day(mid):
                e = mid - 1
            else:
                b = mid + 1
                
        return b
