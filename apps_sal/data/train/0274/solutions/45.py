class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
#         minheap=[]
#         maxheap=[]
#         heapq.heapify(minheap)
#         heapq.heapify(maxheap)
#         length=1
#         i=0
#         j=1
#         heapq.heappush(minheap,[nums[0],0]) # add first element and its index
#         heapq.heappush(maxheap,[-nums[0],0])
#         while j < len(nums):
#             if nums[j]-minheap[0][0]<=limit and maxheap[0][0]*-1-nums[j]<= limit:
#                 length=max(length,j-i+1)
#                 heapq.heappush(minheap,[nums[j],j])
#                 heapq.heappush(maxheap,[-nums[j],j])
#                 j=j+1
#             else:
#                 while len(minheap)>0 and nums[j]-minheap[0][0]>limit:
#                     ele,index=heapq.heappop(minheap)
#                     i=max(i,index + 1)
#                 while len(maxheap)>0 and -maxheap[0][0]-nums[j]>limit:
#                     ele,index=heapq.heappop(maxheap)
#                     i=max(i,index + 1)
#                 # i=maxindex+1   # update i and now  we are not concerned with element before ith index
#                 heapq.heappush(minheap,[nums[j],j]) # add  element and its index
#                 heapq.heappush(maxheap,[-nums[j],j])
#                 j=j+1
            
#         return length
        begin = end = 0
        l = len(nums)
        d = 0
        
        heap_min = []
        heap_max = []
        
        heapq.heapify(heap_min)
        heapq.heapify(heap_max)
        
        while end < l:
            heapq.heappush(heap_min, (nums[end], end))
            heapq.heappush(heap_max, (-1 * nums[end], end))
            
            while len(heap_min) > 0 and nums[end] - heap_min[0][0] > limit:
                value, idx = heapq.heappop(heap_min)
                begin = max(begin, idx + 1)
            
            while len(heap_max) > 0 and -heap_max[0][0] - nums[end] > limit:
                value, idx = heapq.heappop(heap_max)
                begin = max(begin, idx + 1)
            
            if end - begin + 1 > d:
                d = end - begin + 1
            
            end += 1
        return d
