class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0
        pre = 0
        res = 1
        maxs = []
        mins = []
        for i in range(len(nums)):
            while maxs and maxs[-1] < nums[i]:
                maxs.pop()
            while mins and mins[-1] > nums[i]:
                mins.pop()
            maxs.append(nums[i])
            mins.append(nums[i])
            while maxs[0] - mins[0] > limit:
                if maxs[0] == nums[pre]:
                    maxs.pop(0)
                if mins[0] == nums[pre]:
                    mins.pop(0)
                pre += 1
            res = max(res, i - pre + 1)
        return res
