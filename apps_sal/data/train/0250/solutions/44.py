class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        from fractions import Fraction
        workers = sorted([(w/q,q,w) for q,w in zip(quality, wage)])
        
        min_cost = float('inf')
        from queue import PriorityQueue
        pq = PriorityQueue()
        summ = 0
        print(workers)
        for ratio, q, w in workers:
            pq.put(-q)
            summ += q
            
            if pq.qsize() > K:
                summ += pq.get()
            if pq.qsize() == K:
                min_cost = min(min_cost, ratio*summ)
            
        return float(min_cost)
