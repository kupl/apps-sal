# idea: greedy. keep a check of cumulated sum, and as soon as we find a subarray whose sum equals target, we reset cumulated sum

class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        cum_sum = 0
        seen_cum_sum = set([0])
        count = 0
        
        for num in nums:
            cum_sum += num
            complement = cum_sum-target
            
            # if we found a subarray whose sum equals target, we reset cumulated sum
            if complement in seen_cum_sum:
                count += 1
                cum_sum = 0
                seen_cum_sum = set([0])
                
            seen_cum_sum.add(cum_sum)
                
        return count
