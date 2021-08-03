class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        while nums != [0] * len(nums):
            for i in range(len(nums)):
                if nums[i] % 2 == 1:
                    nums[i] -= 1
                    ans += 1
            if nums != [0] * len(nums):
                for i in range(len(nums)):
                    nums[i] //= 2
                ans += 1
        return ans
