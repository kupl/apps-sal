class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not len(nums): return 0
        
        ml, start, end = 1, 0, 0
        pqmin, pqmax = [], []
        
        for end in range(len(nums)):
            heapq.heappush(pqmin, (nums[end], end))
            heapq.heappush(pqmax, (-nums[end], end))
            
            while start < end and abs(pqmax[0][0] + pqmin[0][0]) > limit:# we will pop out numbers until max - min < limit
                start += 1

                while pqmax and pqmax[0][1] < start: heapq.heappop(pqmax) ## I only care if the max number index has been passed, if yes, we should pop out all numbers before that
                while pqmin and pqmin[0][1] < start: heapq.heappop(pqmin)## I only care if the min number index has been passed, if yes, we should pop out all numbers before that
            ml = max(ml, end - start + 1)
            
        return ml

