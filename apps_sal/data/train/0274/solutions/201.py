from sortedcontainers import SortedList


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        lhs = 0
        rhs = 1
        diff_len = 1
        sd = SortedList([nums[lhs]])
        while rhs < len(nums):
            sd.add(nums[rhs])
            if (sd[len(sd) - 1] - sd[0] <= limit):

                diff_len = max(diff_len, rhs - lhs + 1)

            else:
                sd.discard(nums[lhs])
                lhs += 1
            rhs += 1
        return diff_len
