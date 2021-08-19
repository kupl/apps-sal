class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_heap = []
        max_heap = []
        longest_window = 1
        min_idx = 0
        for (i, num) in enumerate(nums):
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            while min_heap[0][1] < min_idx:
                heapq.heappop(min_heap)
            while max_heap[0][1] < min_idx:
                heapq.heappop(max_heap)
            if abs(min_heap[0][0] + max_heap[0][0]) > limit:
                if min_heap[0][1] < max_heap[0][1]:
                    min_idx = min_heap[0][1] + 1
                    heapq.heappop(min_heap)
                else:
                    min_idx = max_heap[0][1] + 1
                    heapq.heappop(max_heap)
            longest_window = max(longest_window, i - min_idx + 1)
        return longest_window
