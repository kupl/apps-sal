class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        
        def isFeasible(days):
            
            bouquetsSoFar = 0
            flowersSoFar = 0
            
            for d in bloomDay:
                
                if d <= days:
                    flowersSoFar += 1
                    if flowersSoFar == k:
                        bouquetsSoFar += 1
                        flowersSoFar = 0
                        if bouquetsSoFar == m:
                            return True
                else:
                    flowersSoFar = 0
                
            return False
        
        if len(bloomDay) < m * k:
            return -1
        
        left, right = min(bloomDay), max(bloomDay)
        
        while left < right:
            
            mid = left + (right - left) // 2
            
            if isFeasible(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
