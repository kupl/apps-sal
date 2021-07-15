class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def odd_2_even(nums):
            step = 0
            new_nums = []
            for i in range(len(nums)):
                if nums[i] % 2 == 1:
                    step += 1
                    nums[i] -= 1
                    if nums[i] > 0:
                        new_nums.append(nums[i])
                elif nums[i] > 0:
                    new_nums.append(nums[i])
            return step,new_nums
        
        def even_2(nums):
            return [a//2 for a in nums]
        
        step = 0
        while len(nums) > 0:
            add,nums = odd_2_even(nums)
            if len(nums) > 0:
                nums = even_2(nums)
                step += 1
            step = step + add
        
        return step
