import heapq as hq


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        if K == 1:
            return min(wage)
        N = len(quality)
        ratio = [(w / q, i) for i, (w, q) in enumerate(zip(wage, quality))]
        ratio.sort()
        quality = [quality[i] for _, i in ratio]
        ratio = [r for r, _ in ratio]
        min_K_queue = [-x for x in quality[: K - 1]]
        hq.heapify(min_K_queue)
        _sum = sum(quality[: K - 1])
        _min = float('inf')
        for k in range(K - 1, N):
            _min = min((_sum + quality[k]) * ratio[k], _min)
            if -quality[k] > min_K_queue[0]:
                poped = hq.heappop(min_K_queue)
                _sum = _sum + poped + quality[k]
                hq.heappush(min_K_queue, -quality[k])
        return _min
