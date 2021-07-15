class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        
        # Taking a walk through the array, if we can ever make the target, we might as well because we'd like the border for the last subarray to be as far left as possible for the next. To see if we can make the target, we just take the total sum so far and see if we ever had the right previous total sum to chop off. We also check that the chop point does not overlap another subarray end point we used.
        #maintain a list of end indices
        hmap = collections.defaultdict(int)
        rsum = 0
        res = 0
        last = -1
        hmap[0] = -1
        
        for index,num in enumerate(nums):
            
            rsum += num
            
            csum = rsum - target
            
            # if rsum == target:
            #     res += 1
            
            if csum in hmap and hmap[csum] >= last:
                res += 1
                last = index
                
            hmap[rsum] = index
            
        return res
