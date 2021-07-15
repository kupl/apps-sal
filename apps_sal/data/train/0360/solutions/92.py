class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def condition(k):
            ind, load, days = 0, 0, 0
            while ind < len(weights):
                #print(ind, load, days)
                if weights[ind] + load <= k:
                    load += weights[ind]
                    ind += 1
                else:
                    load = 0
                    days += 1
            return days + 1 <= D
        
        #print(condition(15))
        
        
        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
    
        

