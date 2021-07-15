class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        #return self.greedy(quality, wage, K)
        return self.heap(quality, wage, K)
        
    def greedy(self, quality, wage, K):
        ans = float('inf')
        
        size = len(quality)
        for captain in range(size):
            ratio = wage[captain] / quality[captain]
            
            prices = []
            for worker in range(size):
                price = ratio * quality[worker]
                if price < wage[worker]:
                    continue
                prices.append(price)
            
            if len(prices) < K:
                continue
            prices.sort()
            ans = min(ans, sum(prices[:K]))
        return float(ans)
    
    def heap(self, quality, wage, K):
        
        workers = sorted(( w / q, q, w) for q, w in zip(quality, wage))
        
        ans = float('inf')
        myHeap = []
        qualitySum = 0
        for ratio, q, w in workers:
            heapq.heappush(myHeap, -q)
            qualitySum += q
            
            if len(myHeap) > K:
                qualitySum += heapq.heappop(myHeap)
            
            if len(myHeap) == K:
                ans = min(ans, ratio * qualitySum)
        return float(ans)
