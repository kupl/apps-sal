class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        output, nums = 0, sorted(nums)
        while l <= r:
            if nums[l] + nums[r] <= target:
                output += pow(2, r - l, 10 ** 9 + 7)
                l += 1
            else:
                r -= 1
        return output % (10 ** 9 + 7)
