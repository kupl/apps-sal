class Solution:

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        while True:
            zeros = 0
            ans += 1
            for (i, num) in enumerate(nums):
                nums[i] = num // 2
                ans += num % 2
                if not nums[i]:
                    zeros += 1
            if zeros == n:
                break
        return ans - 1
