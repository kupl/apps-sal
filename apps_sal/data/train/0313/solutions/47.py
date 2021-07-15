class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def feasible(day):
            
            bou = 0
            flowers = 0
            
            for bloom in bloomDay:
                if bloom > day:
                    flowers = 0
                else:
                    bou += (flowers+1)//k
                    flowers = (flowers+1)%k
            
            
            if bou < m:
                return False
            return True
        
        if len(bloomDay) < (m*k):
            return -1
        
        left = 1
        right = max(bloomDay)
        
        while left < right :
            mid = (left+right)//2
            
            if feasible(mid):
                right = mid
            else: left = mid + 1
                
        return left
