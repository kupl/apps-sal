class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = count = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:    
                count += 2 ** (r - l)
                l += 1
        return count % (10 ** 9 + 7)
            
            
             
            

