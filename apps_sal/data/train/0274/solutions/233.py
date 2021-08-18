import heapq


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        minheap = []
        maxheap = []
        heapq.heapify(minheap)
        heapq.heapify(maxheap)

        heapq.heappush(minheap, [nums[0], 0])
        heapq.heappush(maxheap, [-nums[0], 0])

        begin = 0
        length = 1
        end = 1
        next_idx = 0
        while begin <= end and end <= len(nums) - 1:

            if abs(minheap[0][0] - nums[end]) <= limit and abs(abs(maxheap[0][0]) - nums[end]) <= limit:
                length = max(length, (end - begin) + 1)

            else:
                while len(minheap) > 0 and abs(minheap[0][0] - nums[end]) > limit:
                    ele, idx = heapq.heappop(minheap)
                    next_idx = max(next_idx, idx)
                while len(maxheap) > 0 and abs(-maxheap[0][0] - nums[end]) > limit:
                    ele, idx = heapq.heappop(maxheap)
                    next_idx = max(next_idx, idx)
                begin = next_idx + 1
            heapq.heappush(minheap, [nums[end], end])
            heapq.heappush(maxheap, [-nums[end], end])
            end += 1
        return length
