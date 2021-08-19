class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0
        (min_heap, max_heap) = ([], [])
        (res, i) = (0, 0)
        for (j, num) in enumerate(nums):
            heapq.heappush(min_heap, [num, j])
            heapq.heappush(max_heap, [-num, j])
            while abs(min_heap[0][0] + max_heap[0][0]) > limit:
                i = min(min_heap[0][1], max_heap[0][1]) + 1
                while min_heap[0][1] < i:
                    heapq.heappop(min_heap)
                while max_heap[0][1] < i:
                    heapq.heappop(max_heap)
            res = max(res, j - i + 1)
        return res
