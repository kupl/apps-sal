class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        while sum(nums) != 0:
            for i in range(len(nums)):
                if nums[i] % 2 == 1:
                    nums[i] -= 1
                    res += 1
            if sum(nums) != 0:
                for i in range(len(nums)):
                    nums[i]  /= 2
                res += 1
            # print(nums)
        return res

