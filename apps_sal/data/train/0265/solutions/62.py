class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        d = {0: -1}
        add = 0
        count = 0
        i = 0
        while(i <= len(nums) - 1):
            add += nums[i]
            if (add - target) in d:
                count += 1
                d = {}
            d[add] = i
            i += 1
        return count
