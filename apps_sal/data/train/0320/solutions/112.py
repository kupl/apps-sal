class Solution:

    def minOperations(self, nums) -> int:
        res = 0
        N = len(nums)
        while True:
            for (i, v) in enumerate(nums):
                if v & 1:
                    res += 1
                    nums[i] -= 1
            if nums == [0] * N:
                return res
            for i in range(N):
                nums[i] //= 2
            res += 1
        return res
