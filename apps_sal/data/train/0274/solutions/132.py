import heapq

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        longest = 0
        minHeap = []
        maxHeap = []
        front = -1
        back = 0
        while back < len(nums):
            needsShrinking = False
            if front < len(nums) - 1:
                front += 1
                heapq.heappush(minHeap, (nums[front], front))
                heapq.heappush(maxHeap, (-nums[front], front))
            else:
                needsShrinking = True
                
            while needsShrinking or (minHeap and maxHeap and abs(minHeap[0][0] + maxHeap[0][0]) > limit):
                needsShrinking = False
                back += 1
                while minHeap and minHeap[0][1] < back: heapq.heappop(minHeap)
                while maxHeap and maxHeap[0][1] < back: heapq.heappop(maxHeap)
            
            longest = max(longest, front - back + 1)
            
        return longest
