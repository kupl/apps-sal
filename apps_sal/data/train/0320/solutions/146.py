class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        while any(nums):
            for i, x in enumerate(nums):
                if x % 2 == 1:
                    nums[i] -= 1
                    ans += 1
            if any(nums):
                for i, x in enumerate(nums):
                    nums[i] //= 2
                ans += 1
        return ans
