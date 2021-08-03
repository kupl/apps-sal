class Solution:
    def minOperations(self, nums: List[int]) -> int:

        ans = 0

        while sum(nums) != 0:
            count_odd = 0
            for i, num in enumerate(nums):
                if num % 2 != 0:
                    count_odd += 1
                    ans += 1
                    nums[i] = nums[i] - 1

            if count_odd == 0:
                for i in range(len(nums)):
                    nums[i] = nums[i] // 2
                ans += 1

        return ans
