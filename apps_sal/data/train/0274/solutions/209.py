import heapq


class Item:
    (val, index) = (0, 0)

    def __lt__(self, other):
        return self.val < other.val

    def __init__(self, val, index):
        self.val = val
        self.index = index


class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        (maxheap, minheap) = ([], [])
        index = 0
        maxLen = 0
        leftIndex = -1
        while index < len(nums):
            while len(minheap) > 0 and (minheap[0].val < nums[index] - limit or minheap[0].index < leftIndex):
                leftIndex = max(leftIndex, heapq.heappop(minheap).index)
            while len(maxheap) > 0 and (-maxheap[0].val > nums[index] + limit or maxheap[0].index < leftIndex):
                leftIndex = max(leftIndex, heapq.heappop(maxheap).index)
            heapq.heappush(minheap, Item(nums[index], index))
            heapq.heappush(maxheap, Item(-nums[index], index))
            maxLen = max(maxLen, index - leftIndex)
            index += 1
        return maxLen
