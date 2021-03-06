import heapq


class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not len(nums):
            return 0
        output = 1
        s_idx = 0
        e_idx = 0
        pqmin = []
        pqmax = []
        for e_idx in range(len(nums)):
            heapq.heappush(pqmin, (nums[e_idx], e_idx))
            heapq.heappush(pqmax, (-nums[e_idx], e_idx))
            while s_idx < e_idx and abs(pqmax[0][0] + pqmin[0][0]) > limit:
                s_idx += 1
                while pqmax and pqmax[0][1] < s_idx:
                    heapq.heappop(pqmax)
                while pqmin and pqmin[0][1] < s_idx:
                    heapq.heappop(pqmin)
            output = max(output, e_idx - s_idx + 1)
        return output
