class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        combine = sorted([(wage[i] / quality[i], quality[i]) for i in range(len(quality))], key=lambda x: (-x[0], x[1]))
        tc = float('inf')
        n = len(combine)
        q = []
        heapq.heapify(q)
        for i in range(len(combine) - 1, -1, -1):
            heapq.heappush(q, -combine[i][1])
            if len(q) > K:
                heapq.heappop(q)
            if i <= n - K:
                tc = min(tc, -combine[i][0] * sum(q))
        return tc
