class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        while True:
            for i in range(N):
                res += nums[i] % 2
                nums[i] = (nums[i] - nums[i] % 2) // 2
            if all(n == 0 for n in nums):
                return res
            res += 1

