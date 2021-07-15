class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        #Lower bound has to be the maximum of the weight to ship all weights
        #Upper bound is the sum of the weights (can ship all packages in one day)
        left= max(weights)
        right =sum(weights)
        
        #Finding a weight which is between lower and upper value
        while left <= right:
            
            #days_needed helps to calculate how many days can be covered with the weight chosen
            #cur tells us the sum of all the weights for the day
            mid, days_needed, cur = int((left + right) / 2), 1, 0 
            
            #mid is the weight which is chosen to divide all the other wirghts in days
            #loop through each weight
            for w in weights:
                if cur + w > mid:
                    days_needed += 1
                    cur = 0
                cur += w
                
            if days_needed > D: 
                left = mid + 1
                
            else: 
                right = mid-1
                
        return left #why is left returned? anything can be returned whether its left or right
