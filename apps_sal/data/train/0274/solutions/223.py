from sortedcontainers import SortedList


class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0
        pq_min = SortedList([])
        pq_max = SortedList([])
        (st, end, res) = (0, 0, 0)
        for val in nums:
            pq_min.add(val)
            pq_max.add(-val)
            end += 1
            while abs(pq_min[0] + pq_max[0]) > limit:
                pq_min.remove(nums[st])
                pq_max.remove(-nums[st])
                st += 1
            res = max(res, end - st)
        return res
