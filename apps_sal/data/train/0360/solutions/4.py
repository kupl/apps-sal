class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        lo = 0 
        hi = 0
        for i in range(len(weights)):
            lo = max(lo,weights[i])
            hi = hi + weights[i]
        
        optimalcapacity =hi+1
        while lo<=hi:
            days =1
            capacity = 0
            mid = lo + (hi - lo)//2
            for i in range(len(weights)):
                if weights[i] + capacity > mid:
                    days= days+1
                    capacity = weights[i]
                else:
                    capacity+=weights[i]
            if days <= D:
                hi = mid -1
                optimalcapacity= min(optimalcapacity,mid)
            else:
                lo = mid+1
        return optimalcapacity        
            
            
            

