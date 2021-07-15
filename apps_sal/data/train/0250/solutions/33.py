class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        n = len(quality)
        
        # 1. compute wage per quality for each worker i
        wage_per_qual = []
        for i in range(n):
            wage_per_qual.append(wage[i] / quality[i])
        
        # 2. sort wage per quality (sort worker index)
        workers = sorted(list(range(n)), key=lambda i: wage_per_qual[i])
        
        # 3. max heap keep track of minimum k quality
        max_heap = []
        # current total quality so far
        total_quality = 0
        
        min_total = float('inf')
        for w in workers:
            if len(max_heap) < K:
                total_quality += quality[w]
                heapq.heappush(max_heap, -quality[w])
                if len(max_heap) == K:
                    min_total = min(min_total, wage_per_qual[w]*total_quality)
            else:
                if quality[w] < -max_heap[0]:
                    neg_qual = heapq.heappushpop(max_heap, -quality[w])
                    total_quality += neg_qual + quality[w]
                    # # pop the maximum quality to add current worker
                    # neg_qual = heapq.heappop(max_heap)
                    # # remove previous max quality
                    # total_quality += neg_qual
                    # # add current quality
                    # total_quality += quality[w]
                    # heapq.heappush(max_heap, -quality[w])
                    
                    # use current worker as the base wage
                    min_total = min(min_total, wage_per_qual[w]*total_quality)
        
        return min_total

