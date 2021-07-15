class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_heap = []
        max_heap = []
        start = 0
        best = 0
        for idx, val in enumerate(nums):
            heappush(min_heap, (val, idx))
            heappush(max_heap, (-val, idx))

            while start < idx and abs(min_heap[0][0] + max_heap[0][0]) > limit:
                start += 1
                while min_heap[0][1] < start:
                    heappop(min_heap)
                while max_heap[0][1] < start:
                    heappop(max_heap)
            best = max(best, idx - start + 1)
        return best
