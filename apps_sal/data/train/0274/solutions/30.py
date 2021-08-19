class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        (max_heap, min_heap) = ([], [])
        res = 0
        l = 0
        for (r, a) in enumerate(nums):
            heapq.heappush(max_heap, [-a, r])
            heapq.heappush(min_heap, [a, r])
            while -max_heap[0][0] - min_heap[0][0] > limit:
                while max_heap[0][1] <= l:
                    heapq.heappop(max_heap)
                while min_heap[0][1] <= l:
                    heapq.heappop(min_heap)
                l += 1
            res = max(res, r - l + 1)
        return res
