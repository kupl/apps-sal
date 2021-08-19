class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxq, minq = [], []
        l, r = 0, 0
        res = 0
        for r in range(len(nums)):
            heapq.heappush(maxq, [-nums[r], r])
            heapq.heappush(minq, [nums[r], r])
            while -maxq[0][0] - minq[0][0] > limit:
                # condition not satisfied, move left pointer ahead
                l = min(maxq[0][1], minq[0][1]) + 1
                # all values before left pointer are now useless
                while maxq[0][1] < l:
                    heapq.heappop(maxq)
                while minq[0][1] < l:
                    heapq.heappop(minq)
            res = max(res, r - l + 1)
        return res
