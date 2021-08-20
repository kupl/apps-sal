class Solution:

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        n = len(quality)
        wage_per_qual = []
        for i in range(n):
            wage_per_qual.append(wage[i] / quality[i])
        workers = sorted(list(range(n)), key=lambda i: wage_per_qual[i])
        max_heap = []
        total_quality = 0
        min_total = float('inf')
        for w in workers:
            if len(max_heap) < K:
                total_quality += quality[w]
                heapq.heappush(max_heap, -quality[w])
                if len(max_heap) == K:
                    min_total = min(min_total, wage_per_qual[w] * total_quality)
            elif quality[w] < -max_heap[0]:
                neg_qual = heapq.heappushpop(max_heap, -quality[w])
                total_quality += neg_qual + quality[w]
                min_total = min(min_total, wage_per_qual[w] * total_quality)
        return min_total
