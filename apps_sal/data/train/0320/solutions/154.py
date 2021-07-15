class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        
        while not(self.is_end(nums)):
            ops += self.perform_decrement(nums)
            if self.is_end(nums): return ops
            ops += self.perform_division(nums)
        return ops
        #jesli nieparzytte to odejmij 1
        #jesli wszystkie parzyste to podziel
        
    def is_end(self, nums):
        return all(i == 0 for i in nums)
    
    def perform_decrement(self, nums):
        ops = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                nums[i] -= 1
                ops += 1
        return ops

    def perform_division(self, nums):
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i] //= 2
        return 1
                

