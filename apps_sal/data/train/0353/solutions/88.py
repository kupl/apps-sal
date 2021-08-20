class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        (left, right) = (0, len(nums) - 1)
        power_set = 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                power_set += 2 ** (right - left)
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
        return power_set % (10 ** 9 + 7)
