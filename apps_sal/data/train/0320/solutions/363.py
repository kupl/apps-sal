class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0        
        while sum(nums) != 0:
            for i in range(len(nums)):
                if nums[i] % 2 != 0:
                    nums[i] = nums[i] - 1
                    res += 1
            # print([x % 2 for x in nums])
            if sum([x % 2 for x in nums]) == 0:
                for i in range(len(nums)):
                    nums[i] = nums[i] / 2
                res += 1
        return res - 1
        
                


