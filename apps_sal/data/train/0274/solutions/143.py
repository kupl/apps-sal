import heapq


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_heap = []
        max_heap = []
        i, j = 0, 0
        res = 0
        while i < len(nums) and j < len(nums):
            heapq.heappush(min_heap, (nums[j], j))
            heapq.heappush(max_heap, (-nums[j], j))
            while -max_heap[0][0] - min_heap[0][0] > limit:
                i = min(i, min_heap[0][1], max_heap[0][1]) + 1
                while max_heap[0][1] < i:
                    heapq.heappop(max_heap)
                while min_heap[0][1] < i:
                    heapq.heappop(min_heap)
            res = max(res, j - i + 1)
            j += 1
        return res
