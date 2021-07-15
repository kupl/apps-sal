class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        ## Function to check required bouquets can be made 
        ## within the parameterized number of days.
        def canMakeBouquet(m, k, bloomDay, currDay):
            
            ## Variable for keeping track of 
            ## the number of bouquets made.
            numBouquets = 0
            
            ## Variable for sliding window length.
            slidingWindowLen = 0
            
            for i in range(0, len(bloomDay)):
                
                ## Check whether the flower has bloomed or not.
                if (bloomDay[i] <= currDay):
                    slidingWindowLen += 1
                else:
                    slidingWindowLen = 0
                    
                ## Check whether a bouquet can be constructed.
                if (slidingWindowLen == k):
                    numBouquets += 1
                    slidingWindowLen = 0
                    
            ## Check whether sufficient bouquets can be made.
            return (numBouquets >= m)
        
        ## return canMakeBouquet(m, k, bloomDay, 4)
        
        ## Initialise binary search bounds.
        lowBound = 1
        highBound = max(bloomDay)
        
        ## Perform Binary Search.
        while (lowBound < highBound):
            
            ## Compute the midBound.
            midBound = lowBound + (highBound - lowBound)//2
            
            ## If bouquets cannot be made.
            if (not canMakeBouquet(m, k, bloomDay, midBound)):
                lowBound = midBound + 1
            else:
                highBound = midBound
                
        ## Perform sanity check.
        if (canMakeBouquet(m, k, bloomDay, lowBound)):
            return lowBound
        else:
            return -1
            

