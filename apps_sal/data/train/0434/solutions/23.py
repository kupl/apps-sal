class Solution:

    def longestSubarray(self, nums: List[int]) -> int:
        res = zeros = zero_i = i = 0
        for (j, v) in enumerate(nums):
            if v == 0:
                zeros += 1
                if zeros == 2:
                    i = zero_i + 1
                    zeros = 1
                zero_i = j
            res = max(res, j - i)
        return res
