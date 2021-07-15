class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def condition(capacity):
            day = 1
            increaseCap = 0
            i=0
            while i < len(weights):
                increaseCap +=weights[i]
                if increaseCap > capacity:
                    increaseCap = weights[i]
                    day+=1
                    if day > D: return False
                i+=1
            return True 
        
        left , right  = max(weights), sum(weights)
        while left < right:
            mid =  left + (right - left) //2
            if condition(mid):
                right = mid
            else:
                left = mid+1
        return left

