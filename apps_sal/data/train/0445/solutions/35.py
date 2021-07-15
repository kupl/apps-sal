class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 5:
            return 0
        # nums.sort()
        # return min(nums[-4]-nums[0], nums[-3]-nums[1], nums[-2]-nums[2], nums[-1]-nums[3])
        
        l = []
        h = []
        
        for c in nums:
            heapq.heappush(l, -c)
            if len(l) > 4:
                heapq.heappop(l)
            heapq.heappush(h, c)
            if len(h) > 4:
                heapq.heappop(h)
        
        l = [-c for c in l]
        l.sort()
        h.sort()
        
        return min(h[0]-l[0], h[1]-l[1], h[2]-l[2], h[3]-l[3])
