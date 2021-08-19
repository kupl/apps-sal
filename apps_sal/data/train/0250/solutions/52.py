class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        combine = sorted([(wage[i] / quality[i], quality[i]) for i in range(len(quality))], key=lambda x: (-x[0], x[1]))
        # combine =  sorted([(quality[i],wage[i]/quality[i]) for i in range(len(quality))])
        qual = [e[1] for e in combine]
        rates = [e[0] for e in combine]
        tc = float('inf')
        n = len(combine)
        q = []
        heapq.heapify(q)
        for i in range(len(combine) - 1, -1, -1):
            # if i < K-1: return tc
            heapq.heappush(q, -qual[i])
            if len(q) > K:
                heapq.heappop(q)
            if i <= n - K:
                tc = min(tc, -rates[i] * sum(q))

        return tc
