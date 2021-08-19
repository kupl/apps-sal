from sortedcontainers import SortedList


class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0
        sl = SortedList([])
        (st, end, res) = (0, 0, 0)
        for val in nums:
            sl.add(val)
            end += 1
            while abs(sl[0] - sl[-1]) > limit:
                sl.remove(nums[st])
                st += 1
            res = max(res, end - st)
        return res
