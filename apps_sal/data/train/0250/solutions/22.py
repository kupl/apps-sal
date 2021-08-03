class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        # rate, q, w
        q_w = [(w / q, q, w) for q, w in zip(quality, wage)]
        q_w.sort()
        curr = sum([q_w[i][1] for i in range(K)])
        heap = [-q_w[i][1] for i in range(K)]
        heapq.heapify(heap)
        r = q_w[K - 1][0]
        res = r * curr
        for r, q, w in q_w[K:]:
            curr += q
            heapq.heappush(heap, -q)
            curr += heapq.heappop(heap)
            res = min(res, curr * r)
        return res
