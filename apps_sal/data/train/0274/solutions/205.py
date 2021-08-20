class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxq = []
        minq = []
        left = 0
        res = 0
        for i in range(len(nums)):
            heapq.heappush(maxq, [-nums[i], i])
            heapq.heappush(minq, [nums[i], i])
            while -maxq[0][0] - minq[0][0] > limit:
                left = min(maxq[0][1], minq[0][1]) + 1
                while maxq[0][1] < left:
                    heapq.heappop(maxq)
                while minq[0][1] < left:
                    heapq.heappop(minq)
            res = max(res, i - left + 1)
        return res
