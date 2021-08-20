class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minheap = []
        maxheap = []
        heapq.heapify(minheap)
        heapq.heapify(maxheap)
        length = 1
        i = 0
        j = 1
        heapq.heappush(minheap, [nums[0], 0])
        heapq.heappush(maxheap, [-nums[0], 0])
        while j < len(nums):
            if nums[j] - minheap[0][0] <= limit and maxheap[0][0] * -1 - nums[j] <= limit:
                length = max(length, j - i + 1)
                heapq.heappush(minheap, [nums[j], j])
                heapq.heappush(maxheap, [-nums[j], j])
                j = j + 1
            else:
                while len(minheap) > 0 and abs(minheap[0][0] - nums[j]) > limit:
                    (ele, index) = heapq.heappop(minheap)
                    i = max(i, index + 1)
                while len(maxheap) > 0 and abs(-maxheap[0][0] - nums[j]) > limit:
                    (ele, index) = heapq.heappop(maxheap)
                    i = max(i, index + 1)
                heapq.heappush(minheap, [nums[j], j])
                heapq.heappush(maxheap, [-nums[j], j])
                j = j + 1
        return length
