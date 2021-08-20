class Solution:

    def minOperations(self, nums: List[int]) -> int:
        res = 0
        mask = 2 ** 32 - 2
        for _ in range(32):
            end = True
            for (i, x) in enumerate(nums):
                res += x & 1
                nums[i] >>= 1
                if nums[i]:
                    end = False
            if end:
                break
            res += 1
        return res
