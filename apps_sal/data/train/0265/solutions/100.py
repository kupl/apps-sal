class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        # if nums[0:j] sum larger than target and there is a subarry nums[i:j] sum equal to target
        # then sum(0:j)-sum(0:i) == target
        # base on this idea, we could store each prefix_sum in to a map, 
        # check whether sum(0:j)-target is in the prefix_sum map. 
        # since we need overlapping, so store the right_most index for each prefix sum
        # update the just found subarry's rightmose index, check current end index
        
        map = {0:-1}
        prefix, rightmost, count = 0, -1, 0
        
        for i,val in enumerate(nums):
            prefix += val
            if prefix-target in map and map[prefix-target]>=rightmost: # for overlapping
                count += 1
                rightmost = i
                
            map[prefix] = i
            
        return count

