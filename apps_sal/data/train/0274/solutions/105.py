from heapq import heappush,heappop
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        i = j = best = 0
        minHeap, maxHeap = [], []

        while j < len(nums):
            heappush(minHeap,(nums[j],j))
            heappush(maxHeap,(-nums[j],j))
            
            while abs(nums[j] + maxHeap[0][0]) > limit:
                i = max(i, heappop(maxHeap)[1] + 1)
            while abs(nums[j] - minHeap[0][0]) > limit:
                i = max(i, heappop(minHeap)[1] + 1)
            j+= 1
            best = max(best, j - i)
        return best

