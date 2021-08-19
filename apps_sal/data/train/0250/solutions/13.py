class Solution:

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        ratio = sorted(((w / q, q) for (w, q) in zip(wage, quality)))
        h = []
        (s, res) = (0, float('inf'))
        for (r, q) in ratio:
            heapq.heappush(h, -q)
            s += q
            if len(h) > K:
                s += heapq.heappop(h)
            if len(h) == K:
                res = min(res, r * s)
        return res
