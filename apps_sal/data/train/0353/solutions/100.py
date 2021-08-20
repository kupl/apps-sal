class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        nums.sort()
        result = 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] + nums[right] <= target:
                result += 2 ** (right - left)
                left += 1
            else:
                right -= 1
        return result % (10 ** 9 + 7)
