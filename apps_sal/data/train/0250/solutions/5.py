import heapq


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        n_workers = len(wage)
        pairs = [None] * n_workers
        for i in range(n_workers):
            pairs[i] = (quality[i], wage[i] / quality[i])

        pairs = sorted(pairs, key=lambda x: (x[1]))

        sum_q = sum([p[0] for p in pairs[0:K]])
        maxheap_q = [-p[0] for p in pairs[0:K]]
        heapq.heapify(maxheap_q)
        min_cost = sum_q * pairs[K - 1][1]

        for i in range(K, n_workers):
            sum_q = sum_q - (-min(maxheap_q)) + pairs[i][0]
            min_cost = min(min_cost, sum_q * pairs[i][1])
            heapq.heapreplace(maxheap_q, -pairs[i][0])

        return min_cost
