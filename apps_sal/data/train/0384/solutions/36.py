class Solution:
    def sumSubseqWidths(self, nums):
        res = 0
        for i, num in enumerate(sorted(nums)):
            res += ((1 << i) - (1 << len(nums) - i - 1)) * num

        return res % 1000000007
