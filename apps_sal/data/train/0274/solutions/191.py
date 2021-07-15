class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        maxheap, minheap = [(-nums[0], 0)], [(nums[0], 0)]
        
        l, res  = 0, 1
        for i, val in enumerate(nums[1:], 1): 
               
            if val - minheap[0][0] <= limit and - maxheap[0][0] -val <= limit:
                res = max(res, i - l + 1)
            else:
                
                while minheap and val - minheap[0][0] > limit:
                    v, index = heapq.heappop(minheap)
                    l = max(l, index + 1)
                while maxheap and -maxheap[0][0] - val > limit:
                    v, index = heapq.heappop(maxheap)
                    l = max(l, index + 1)
            
            heapq.heappush(minheap, (val, i))
            heapq.heappush(maxheap, (-val, i))
            
        return res 

