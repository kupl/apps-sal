class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0
        res = i = 0
        maxh = []
        minh = []
        for j, val in enumerate(nums):
            heapq.heappush(maxh, [-val, j])
            heapq.heappush(minh, [val, j])
            while -maxh[0][0] - minh[0][0] > limit:
                i = min(maxh[0][1], minh[0][1]) + 1
                while maxh[0][1] < i:
                    heapq.heappop(maxh)
                while minh[0][1] < i:
                    heapq.heappop(minh)
            res = max(res, j - i + 1)
        return res
                
            
        
        

