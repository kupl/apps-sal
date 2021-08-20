class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        (i, j) = (0, len(nums) - 1)
        res = 0
        while i <= j:
            while i <= j and nums[i] + nums[j] > target:
                j -= 1
            if i <= j and nums[i] + nums[j] <= target:
                res += 2 ** (j - i)
            i += 1
        return res % (10 ** 9 + 7)
