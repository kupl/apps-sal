class Solution:

    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        while any(nums):
            ans += sum((n % 2 for n in nums))
            if any((n > 1 for n in nums)):
                ans += 1
            for i in range(len(nums)):
                nums[i] //= 2
        return ans
