class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxq, minq = [], []
        res = i = 0
        for j, a in enumerate(nums):
            heapq.heappush(maxq, [-a, j])
            heapq.heappush(minq, [a, j])
            while -maxq[0][0] - minq[0][0] > limit:
                i = min(maxq[0][1], minq[0][1]) + 1
                while maxq[0][1] < i:
                    heapq.heappop(maxq)
                while minq[0][1] < i:
                    heapq.heappop(minq)
            res = max(res, j - i + 1)
        return res
