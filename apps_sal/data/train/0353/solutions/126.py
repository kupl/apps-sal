class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        low = 0
        high = len(nums) - 1
        total = 0
        while low < len(nums):
            while high > low and nums[low] + nums[high] > target:
                high -= 1
            s = nums[low] + nums[high]
            if s > target:
                break
            total += 2 ** (high - low)
            low += 1
            high = max(high, low)
        return total % (10 ** 9 + 7)
