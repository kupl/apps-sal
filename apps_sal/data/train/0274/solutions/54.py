class Solution:
    def longestSubarray(self, A: List[int], limit: int) -> int:
        import heapq
        maxd = []
        mind = []
        res = i = 0

        for j, a in enumerate(A):
            heapq.heappush(maxd, [-a, j])
            heapq.heappush(mind, [a, j])
            while - maxd[0][0] - mind[0][0] > limit:
                i = min(maxd[0][1], mind[0][1]) + 1
                while maxd[0][1] < i:
                    heapq.heappop(maxd)
                while mind[0][1] < i:
                    heapq.heappop(mind)
            res = max(res, j - i + 1)
        return res
