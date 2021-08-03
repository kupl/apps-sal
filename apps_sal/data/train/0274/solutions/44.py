class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxq = []
        minq = []
        res = 0
        i = 0
        for j, c in enumerate(nums):
            heapq.heappush(maxq, [-c, j])
            heapq.heappush(minq, [c, j])
            while -maxq[0][0] - minq[0][0] > limit:
                i = min(maxq[0][1], minq[0][1]) + 1
                while maxq[0][1] < i:
                    heapq.heappop(maxq)
                while minq[0][1] < i:
                    heapq.heappop(minq)
            res = max(res, j - i + 1)
        return res
