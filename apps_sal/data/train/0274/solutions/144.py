class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxs, mins = [], []

        res = 0
        start = 0
        for i, n in enumerate(nums):
            while maxs and maxs[-1] < n:
                maxs.pop()

            while mins and mins[-1] > n:
                mins.pop()

            maxs.append(n)
            mins.append(n)

            while maxs[0] - mins[0] > limit:
                if maxs[0] == nums[start]:
                    maxs.pop(0)
                if mins[0] == nums[start]:
                    mins.pop(0)
                start += 1

            res = max(res, i - start + 1)
        return res
