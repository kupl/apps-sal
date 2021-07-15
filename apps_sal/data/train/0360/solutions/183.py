class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        # do a binary search
        # return has to do with weights
        # so initialize right = sum(weights)
        # a ship that can carry everything
        
        left = max(weights)
        right = sum(weights) # this ship over-carries for sure
        
        while left < right:
            # keep track of days
            # if we ship all packages and days too little, it means
            # we can afford to decrease our ship-capacity
            # which means right=mid
            
            # else if days too much,
            # we must increase our ship-capacity
            # so left = mid
            
            # mid is our current ship capacity
            

            mid = (left+right) // 2
            
            days_needed = 1
            cargo = 0
            
            for w in weights:
                if cargo + w > mid:
                    # cannot fit this next package to current cargo
                    days_needed += 1
                    cargo = w
                else:
                    # can fit
                    cargo += w

            
            if days_needed > D:
                # this means it must be greater than mid, for sure
                left = mid + 1
            else:
                right = mid
                
            
        return left
