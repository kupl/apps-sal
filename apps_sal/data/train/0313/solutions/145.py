class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        if len(bloomDay) < m*k:
            return -1
        
        def can_make(days):
            flowers = 0
            bouq = 0
            for i in bloomDay:
                if i > days:
                    flowers = 0
                else:
                    flowers += 1
                
                if flowers == k:
                    bouq += 1
                    flowers = 0
            
            return bouq >=m
                    
        
        left , right = 1 , max(bloomDay)
        while left < right:
            mid = left + (right- left) // 2
            
            if can_make(mid):
                right = mid
            
            else:
                left = mid + 1
        
        return left
