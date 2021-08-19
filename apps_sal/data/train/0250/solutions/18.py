class Solution:

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        workers = []
        for (q, w) in zip(quality, wage):
            workers.append((w / q, q, w))
        workers.sort()
        ans = float('inf')
        dui = []
        sumq = 0
        for (ratio, q, w) in workers:
            heapq.heappush(dui, -q)
            sumq += q
            if len(dui) > K:
                sumq = sumq + heapq.heappop(dui)
            if len(dui) == K:
                ans = min(ans, ratio * sumq)
        return ans
