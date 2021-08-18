import heapq


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxq, minq = [], []
        res = i = 0

        for j in range(len(nums)):
            heapq.heappush(maxq, (-nums[j], j))
            heapq.heappush(minq, (nums[j], j))
            while -maxq[0][0] - minq[0][0] > limit:
                i = min(maxq[0][1], minq[0][1]) + 1
                while i > maxq[0][1]:
                    heapq.heappop(maxq)
                while i > minq[0][1]:
                    heapq.heappop(minq)

            res = max(res, j - i + 1)
        return res
