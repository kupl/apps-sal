import heapq


class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        (minheap, maxheap) = ([], [])
        start = 0
        res = 0
        for (j, elem) in enumerate(nums):
            heapq.heappush(minheap, (elem, j))
            heapq.heappush(maxheap, (-elem, j))
            while -maxheap[0][0] - minheap[0][0] > limit:
                start = min(minheap[0][1], maxheap[0][1]) + 1
                while maxheap[0][1] < start:
                    heapq.heappop(maxheap)
                while minheap[0][1] < start:
                    heapq.heappop(minheap)
            res = max(res, j - start + 1)
        return res
