class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def feasible(days) -> bool:
            flowers = 0
            bouquets = 0
            
            #loop through the array to check the days to bloom
            for bloom in bloomDay:
                if bloom > days: #we cannot gather any flowers to make the bouquets because the flower are not yet bloomed 
                    flowers = 0
                    
                else: 
                    bouquets += (flowers + 1) // k
                    flowers = (flowers + 1) % k
                    
            return bouquets >= m
        
            
        
        
        #base case: 
        if len(bloomDay) < m * k:
            return -1
        left = 1
        right = max(bloomDay)
        while left < right: 
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
                
            else: 
                left = mid + 1
                
        return left
    

