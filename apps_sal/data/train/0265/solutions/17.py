class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        lookup = {0: -1}
        running_sum = 0
        count = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            if running_sum - target in lookup:
                count += 1
                lookup = {}  # reset the map
            lookup[running_sum] = i
        return count
