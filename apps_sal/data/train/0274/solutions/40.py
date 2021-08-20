class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        (minq, maxq) = ([], [])
        l = 0
        res = 0
        for i in range(len(nums)):
            heapq.heappush(minq, [nums[i], i])
            heapq.heappush(maxq, [-nums[i], i])
            while -maxq[0][0] - minq[0][0] > limit:
                l = min(maxq[0][1], minq[0][1]) + 1
                while maxq[0][1] < l:
                    heapq.heappop(maxq)
                while minq[0][1] < l:
                    heapq.heappop(minq)
            res = max(res, i - l + 1)
        return res
