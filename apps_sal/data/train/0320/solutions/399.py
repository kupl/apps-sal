class Solution:
    def is_divisible(self,nums):
        res = []
        for ix in range(len(nums)):
            if nums[ix] % 2 != 0:
                res.append(ix)
        return res
    
    
    def divide_by_2(self,nums):
        for ix in range(len(nums)):
            nums[ix] = nums[ix] / 2
        
    
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        while nums != [0] * len(nums):
            minus_ix = self.is_divisible(nums)
            for ix in minus_ix:
                nums[ix] -= 1
                ops += 1
            
            if nums == [0]* len(nums):
                return ops
            
            # divide all by 2
            self.divide_by_2(nums)
            ops += 1
        return ops
