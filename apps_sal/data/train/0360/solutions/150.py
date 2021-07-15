class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = sum(weights)
        
        while(left < right):
            mid = int((left+right)/2)
            print(mid)
            curr_weight = 0
            days = 1
            for w in weights:
                if(curr_weight+w <= mid):
                    curr_weight+= w
                else:
                    curr_weight = w
                    days += 1
            if(days > D):
                left = mid+1
            else:
                right = mid
        
        return left
                    

