class Solution:
    def minOperations(self, nums: List[int]) -> int:

        maxval = max(nums)
        idx = nums.index(maxval)
        ans = 0

        while nums[idx] != 0:
            for i, n in enumerate(nums):
                ans += n % 2  # minus 1 to make all number even
                nums[i] = n - n % 2
            if nums[idx] != 0:
                for i, n in enumerate(nums):  # devide all numbers by 2
                    nums[i] = nums[i] // 2
                ans += 1

        return ans
