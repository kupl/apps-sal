class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        
        def feasible_bloom_day(value):
            total_bouquet = 0
            num_flowers = 0
            
            for bloom in bloomDay:
                # Flower bloomed
                if ((bloom-1) // value) == 0:
                    num_flowers += 1
                
                    if num_flowers == k:
                        total_bouquet += 1
                        num_flowers = 0
                        
                    if total_bouquet == m:
                        return True
                else: 
                    num_flowers = 0
                    
            
            return False
        
        left, right = 1, max(bloomDay)
        
        while left < right:
            mid = left + (right - left) // 2
            
            if feasible_bloom_day(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
