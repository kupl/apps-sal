class Solution:

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        done = [0] * n
        ans = 0
        while nums != done:
            for (i, x) in enumerate(nums):
                if x % 2:
                    nums[i] -= 1
                    ans += 1
            if nums != done:
                for (i, x) in enumerate(nums):
                    nums[i] /= 2
                ans += 1
        return ans
