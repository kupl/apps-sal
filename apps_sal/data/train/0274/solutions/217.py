class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        start = 0
        result = 0
        minHeap = []
        maxHeap = []
        for i in range(len(nums)):
            heapq.heappush(minHeap, [nums[i], i])
            heapq.heappush(maxHeap, [-nums[i], i])
            while -maxHeap[0][0] - minHeap[0][0] > limit:
                start = min(maxHeap[0][1], minHeap[0][1]) + 1
                while minHeap and minHeap[0][1] < start:
                    heapq.heappop(minHeap)
                while maxHeap and maxHeap[0][1] < start:
                    heapq.heappop(maxHeap)
            result = max(result, i - start + 1)
        return result
