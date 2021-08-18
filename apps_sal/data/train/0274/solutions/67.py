import heapq


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        length = len(nums)
        start = 0
        min_heap = []
        max_heap = []

        res = 1
        for i, num in enumerate(nums):
            heapq.heappush(min_heap, (num, -i))
            heapq.heappush(max_heap, (-num, -i))
            while -min_heap[0][1] < start:
                heapq.heappop(min_heap)
            while -max_heap[0][1] < start:
                heapq.heappop(max_heap)

            while -max_heap[0][0] - min_heap[0][0] > limit:
                start += 1
                while -min_heap[0][1] < start:
                    heapq.heappop(min_heap)
                while -max_heap[0][1] < start:
                    heapq.heappop(max_heap)

            res = max(res, i - start + 1)
        return res
