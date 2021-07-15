class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        while any(nums):
            ans += sum(num % 2 for num in nums)
            if any(num > 1 for num in nums):
                ans += 1
            for i in range(len(nums)):
                nums[i] //= 2
        return ans
                    

