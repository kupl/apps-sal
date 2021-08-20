class Solution:

    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        r1 = max(nums[0:-3]) - min(nums[0:-3])
        r2 = max(nums[1:-2]) - min(nums[1:-2])
        r3 = max(nums[2:-1]) - min(nums[2:-1])
        r4 = max(nums[3:]) - min(nums[3:])
        return min(r1, r2, r3, r4)
