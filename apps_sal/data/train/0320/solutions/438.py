class Solution:

    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        while any((num != 0 for num in nums)):
            odd = 0
            for (idx, num) in enumerate(nums):
                if num & 1:
                    nums[idx] -= 1
                    odd += 1
                    ans += 1
            if not odd:
                for (idx, num) in enumerate(nums):
                    nums[idx] = num // 2
                ans += 1
        return ans
