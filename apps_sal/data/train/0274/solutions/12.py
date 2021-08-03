class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxHeap = []
        minHeap = []
        ans = 0
        i = 0
        for j in range(len(nums)):
            heapq.heappush(maxHeap, (-nums[j], j))
            heapq.heappush(minHeap, (nums[j], j))

            while -maxHeap[0][0] - minHeap[0][0] > limit:
                i = min(maxHeap[0][1], minHeap[0][1]) + 1

                while maxHeap[0][1] < i:
                    heapq.heappop(maxHeap)
                while minHeap[0][1] < i:
                    heapq.heappop(minHeap)
            ans = max(ans, j - i + 1)
        return ans
