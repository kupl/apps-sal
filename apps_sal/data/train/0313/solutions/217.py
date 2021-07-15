class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def isPossible(cap):
            bouquets = 0
            flowers = 0
            
           
            for flower in bloomDay:
                if flower <= cap:
                    flowers += 1
                else:
                    flowers = 0
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            if bouquets < m:
                return False
            else:
                return True
            
        
        left = 1
        right = max(bloomDay)
        if m*k > len(bloomDay):
            return -1
        while left < right:
            
            mid = left + (right-left)//2
            
            if isPossible(mid):
                right = mid
            else:
                left = mid + 1
        return left
