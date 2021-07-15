import heapq
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        N = len(nums)
        if N == 0:
            return 0

        minQ = []
        maxQ = []

        l = 0
        maxL = 0
        for r in range(N):
            num = nums[r]

            idx_rightmost = l - 1
            while minQ and (num - minQ[0][0] > limit or minQ[0][1]<=idx_rightmost):
                [val,idx] = heapq.heappop(minQ)
                idx_rightmost = max(idx_rightmost,idx)

            while maxQ and (-maxQ[0][0] - num > limit or maxQ[0][1]<=idx_rightmost):
                [val,idx] = heapq.heappop(maxQ)
                idx_rightmost = max(idx_rightmost,idx)        
            l = idx_rightmost + 1        
            heapq.heappush(minQ, [nums[r],r])
            heapq.heappush(maxQ, [-nums[r],r])
            maxL = max(maxL, r-l+1)

        return maxL

