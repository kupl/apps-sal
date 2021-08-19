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
        maxindex = 0
        while i <= j and j <= len(nums) - 1:
            if abs(minheap[0][0] - nums[j]) <= limit and abs(abs(maxheap[0][0]) - nums[j]) <= limit:
                length = max(length, j - i + 1)
                heapq.heappush(minheap, [nums[j], j])
                heapq.heappush(maxheap, [-nums[j], j])
                j = j + 1
            else:
                while len(minheap) > 0 and abs(minheap[0][0] - nums[j]) > limit:
                    (ele, index) = heapq.heappop(minheap)
                    maxindex = max(maxindex, index)
                while len(maxheap) > 0 and abs(-maxheap[0][0] - nums[j]) > limit:
                    (ele, index) = heapq.heappop(maxheap)
                    maxindex = max(maxindex, index)
                i = maxindex + 1
                heapq.heappush(minheap, [nums[j], j])
                heapq.heappush(maxheap, [-nums[j], j])
                j = j + 1
        return length
