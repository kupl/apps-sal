class Solution:
    def minOperations(self, nums: List[int]) -> int:
        op = 0
        while(len(nums) > 0):
            for i in range(len(nums)):
                if(nums[i] % 2) == 1:
                    nums[i] -= 1
                    op += 1
            nums = list(filter(lambda x: x != 0, nums))
            if(len(nums) > 0):
                nums[:] = [int(x / 2) for x in nums]
                op += 1
        return op
