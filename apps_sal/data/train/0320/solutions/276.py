class Solution:

    def minOperations(self, nums: List[int]) -> int:
        out = 0
        while sum(nums) != 0:
            for i in range(len(nums)):
                if nums[i] % 2 == 1:
                    nums[i] -= 1
                    out += 1
            if sum(nums) == 0:
                break
            for i in range(len(nums)):
                nums[i] /= 2
            out += 1
        return out
