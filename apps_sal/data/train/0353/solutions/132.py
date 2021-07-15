class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1
        mod = (10**9) + 7
        out = 0
        while left<=right:
            if nums[left]+nums[right] > target:
                right -= 1
            elif nums[left]+nums[right]<=target:
                space = right-left
                out += pow(2, space)
                left += 1
             
               
        return out%mod        
