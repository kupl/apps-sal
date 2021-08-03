class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        minheap, maxheap = [], []
        res = 0
        i = 0
        for j, n in enumerate(nums):
            heapq.heappush(minheap, (n, j))
            heapq.heappush(maxheap, (-n, j))
            while -maxheap[0][0] - minheap[0][0] > limit:
                i = min(maxheap[0][1], minheap[0][1]) + 1
                while maxheap[0][1] < i:
                    heapq.heappop(maxheap)
                while minheap[0][1] < i:
                    heapq.heappop(minheap)
            res = max(res, j - i + 1)
        return res
