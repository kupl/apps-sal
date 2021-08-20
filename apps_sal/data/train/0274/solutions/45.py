class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        begin = end = 0
        l = len(nums)
        d = 0
        heap_min = []
        heap_max = []
        heapq.heapify(heap_min)
        heapq.heapify(heap_max)
        while end < l:
            heapq.heappush(heap_min, (nums[end], end))
            heapq.heappush(heap_max, (-1 * nums[end], end))
            while len(heap_min) > 0 and nums[end] - heap_min[0][0] > limit:
                (value, idx) = heapq.heappop(heap_min)
                begin = max(begin, idx + 1)
            while len(heap_max) > 0 and -heap_max[0][0] - nums[end] > limit:
                (value, idx) = heapq.heappop(heap_max)
                begin = max(begin, idx + 1)
            if end - begin + 1 > d:
                d = end - begin + 1
            end += 1
        return d
