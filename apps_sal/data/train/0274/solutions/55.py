class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        begin, end = 0, 0
        n = len(nums)

        heap_min = []
        heapq.heapify(heap_min)
        heap_max = []
        heapq.heapify(heap_max)

        heapq.heappush(heap_min, (nums[0], 0))
        heapq.heappush(heap_max, (-nums[0], 0))

        max_length = 1
        while end < n - 1:
            end += 1
            if abs(nums[end] - heap_min[0][0]) > limit or abs(-heap_max[0][0] - nums[end]) > limit:  # Need to know the min and max
                # Make it valid!
                while len(heap_min) > 0 and nums[end] - heap_min[0][0] > limit:
                    value, idx = heapq.heappop(heap_min)
                    begin = max(begin, idx + 1)
                while len(heap_max) > 0 and -heap_max[0][0] - nums[end] > limit:
                    value, idx = heapq.heappop(heap_max)
                    begin = max(begin, idx + 1)

            heapq.heappush(heap_min, (nums[end], end))
            heapq.heappush(heap_max, (-nums[end], end))

            max_length = max(max_length, end - begin + 1)

        return max_length
