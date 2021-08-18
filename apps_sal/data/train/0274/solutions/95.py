import heapq


class Solution:
    '''def longestSubarray(self, nums: List[int], limit: int) -> int:
        start = 0
        L = []
        maxlen = 0

        for end, item in enumerate(nums):
            bisect.insort(L, item) 
            while L[-1] - L[0] > limit:
                idx = bisect.bisect(L, nums[start]) - 1 
                L.pop(idx) 
                start += 1
            maxlen = max(maxlen, end-start+1)
        return maxlen'''

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxheap = []
        minheap = []
        start = 0
        maxlen = 0

        for end, item in enumerate(nums):
            heapq.heappush(minheap, (item, end))
            heapq.heappush(maxheap, (-item, end))
            while maxheap and minheap and -maxheap[0][0] - minheap[0][0] > limit:
                start = min(maxheap[0][1], minheap[0][1]) + 1
                while maxheap[0][1] < start:
                    heapq.heappop(maxheap)
                while minheap[0][1] < start:
                    heapq.heappop(minheap)
            maxlen = max(maxlen, end - start + 1)

        return maxlen
