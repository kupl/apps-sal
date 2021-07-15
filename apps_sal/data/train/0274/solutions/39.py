class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        res = 0
        maxq = []
        minq = []
        j = 0
        for i,n in enumerate(nums):
            heapq.heappush(maxq, [-n,i] )
            heapq.heappush(minq, [n,i] )
            
            while -maxq[0][0] - minq[0][0] > limit:
                ind = min( maxq[0][1], minq[0][1] )
                while maxq[0][1] <= ind:
                    heapq.heappop(maxq)
                while minq[0][1] <= ind:
                    heapq.heappop(minq)
                j = ind+1
            res = max(res, i - j +1 )
            
        return res
                
        
        
        
        
        
#         res = 0
        
#         i = 0
#         arr = [] # space O(res)
#         for n in nums:  # O(n) time
#             bisect.insort(arr, n) # O(res)
#             while arr[-1] - arr[0] > limit:
#                 ind = bisect.bisect_right(arr, nums[i])  # O( log res )
#                 arr.pop(ind-1)  # O(res)
#                 i += 1
#             res = max(res, len(arr))
            
#         return res
                
        
        
        
        
        

