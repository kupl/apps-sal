class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        while any(nums):
            for i, v in enumerate(nums):
                if v % 2 == 1:
                    nums[i] -= 1
                    ans += 1
            if any(nums):
                ans += 1
                nums = [i / 2 for i in nums]
        return ans
