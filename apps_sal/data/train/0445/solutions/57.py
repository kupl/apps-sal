class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        nums.sort()
        l = nums[0:4]
        r = nums[-4:]
        p = 0
        res = float('inf')
        while p < 4:
            res = min(res, r[p] - l[p])
            p += 1

        return res
