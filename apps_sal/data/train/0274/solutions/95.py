import heapq


class Solution:
    '''def longestSubarray(self, nums: List[int], limit: int) -> int:
        # TC is O(N^2)
        start = 0
        L = []
        maxlen = 0

        for end, item in enumerate(nums):
            # insert the current item in appropriate position
            bisect.insort(L, item) # insort is O(N)
            # if the difference between start and end is more than expected, keep popping the start indexes
            while L[-1] - L[0] > limit:
                #*****bisect will give you the index but it is ALWAYS +1
                idx = bisect.bisect(L, nums[start]) - 1 # logN TC
                L.pop(idx) # pop that shit and recompute max-min difference again
                start += 1
            maxlen = max(maxlen, end-start+1)
        return maxlen'''

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # insort was expesive in above O(N) so use 2 heaps to maintain max and min
        maxheap = []
        minheap = []
        start = 0
        maxlen = 0

        for end, item in enumerate(nums):
            heapq.heappush(minheap, (item, end))
            heapq.heappush(maxheap, (-item, end))
            #print(minheap, maxheap)
            while maxheap and minheap and -maxheap[0][0] - minheap[0][0] > limit:
                # print()
                #print('heap', minheap, maxheap)
                # find the minimum index of max or min
                start = min(maxheap[0][1], minheap[0][1]) + 1
                # it will be either of min or max, make sure to pop shit just above start so we dont have the max and min item below start
                while maxheap[0][1] < start:
                    heapq.heappop(maxheap)
                while minheap[0][1] < start:
                    heapq.heappop(minheap)
                #print('heap', minheap, maxheap)
            maxlen = max(maxlen, end - start + 1)

        return maxlen
