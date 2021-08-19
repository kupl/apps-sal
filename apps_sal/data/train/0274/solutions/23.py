import heapq


class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans = 1
        i = j = 0
        minHeap = [(nums[0], 0)]
        maxHeap = [(-nums[0], 0)]
        while j < len(nums):
            while minHeap[0][1] < i:
                heapq.heappop(minHeap)
            while maxHeap[0][1] < i:
                heapq.heappop(maxHeap)
            if -maxHeap[0][0] - minHeap[0][0] > limit:
                i += 1
            else:
                j += 1
                ans = max(ans, j - i)
                if j < len(nums):
                    heapq.heappush(minHeap, (nums[j], j))
                    heapq.heappush(maxHeap, (-nums[j], j))
        return ans
