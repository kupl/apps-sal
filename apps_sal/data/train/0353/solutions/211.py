class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        ret = 0
        while left <= right and right < len(nums):
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                ret += 2 ** (right - left)
                ret %= 10 ** 9 + 7
                left += 1
        return ret
