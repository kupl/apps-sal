class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        (minHeap, maxHeap) = ([], [])
        result = i = 0
        for j in range(len(nums)):
            heapq.heappush(minHeap, [nums[j], j])
            heapq.heappush(maxHeap, [-nums[j], j])
            while -maxHeap[0][0] - minHeap[0][0] > limit:
                i = min(maxHeap[0][1], minHeap[0][1]) + 1
                while minHeap[0][1] < i:
                    heapq.heappop(minHeap)
                while maxHeap[0][1] < i:
                    heapq.heappop(maxHeap)
            result = max(result, j - i + 1)
        return result
