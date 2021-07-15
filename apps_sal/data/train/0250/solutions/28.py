class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        A = []
        for q,w in zip(quality, wage):
            A.append([q, w/q])
        
        pq,ans = [],float('inf')
        qSum, ratio = 0,0
        for a in sorted(A, key=lambda x:x[1]):
            if len(pq) < K:
                heapq.heappush(pq, [-a[0], a[1]])
                qSum += a[0]
                ratio = a[1]
            else:
                negq = heapq.heappop(pq)[0]
                qSum= qSum + negq + a[0]
                ratio = a[1]
                heapq.heappush(pq, [-a[0], a[1]])
            
            if len(pq) == K:
                ans = min(ans, qSum*ratio)
                
        return ans
