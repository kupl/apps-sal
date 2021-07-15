class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        if nums.count(0) == len(nums):
            return True
        
        idx = nums.index(1)
        ctr = 0
        for num in nums[idx+1:]:
            if num == 1:
                if ctr < k:
                    return False
                ctr = 0
            else:
                ctr+=1
                
        return True
                
                

