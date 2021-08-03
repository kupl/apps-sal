import heapq


class Item:
    val, index = 0, 0

    def __lt__(self, other):
        return self.val < other.val

    def __init__(self, val, index):
        self.val = val
        self.index = index


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxheap, minheap = [], []
        index = 0
        maxLen = 0
        leftIndex = -1
        while index < len(nums):
            if (len(minheap) > 0 and minheap[0].val < nums[index] - limit):
                while len(minheap) > 0 and (minheap[0].val < nums[index] - limit or minheap[0].index < leftIndex):
                    temp = heapq.heappop(minheap)
                    if (temp.index > leftIndex):
                        leftIndex = temp.index
            if len(maxheap) > 0 and (-maxheap[0].val > nums[index] + limit):
                while len(maxheap) > 0 and (-maxheap[0].val > nums[index] + limit or maxheap[0].index < leftIndex):
                    temp = heapq.heappop(maxheap)
                    if (temp.index > leftIndex):
                        leftIndex = temp.index
            heapq.heappush(minheap, Item(nums[index], index))
            heapq.heappush(maxheap, Item(-nums[index], index))
            maxLen = max(maxLen, index - leftIndex)
            index += 1
        return maxLen
