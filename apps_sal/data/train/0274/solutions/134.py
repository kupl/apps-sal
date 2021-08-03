from sortedcontainers import SortedList


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ret, vals = 0, SortedList()
        l, r, n = 0, 0, len(nums)

        while r < n:
            vals.add(nums[r])

            while vals[-1] - vals[0] > limit:
                vals.remove(nums[l])
                l += 1
            r += 1
            ret = max(ret, r - l)
        return ret
