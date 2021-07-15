class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        
        l=[(x,y) for x,y in zip(speed,efficiency)]
        l=sorted(l,key=lambda x: (x[1],-x[0]))
        #efficiency=sorted(efficiency)
        
        ma=0
        q=[]
        s=0
        for i in range(len(l)-1,-1,-1):
            mi=l[i][1]
            
            heapq.heappush(q,l[i][0])
            s+=l[i][0]
            if len(q)>k:
                s-=heapq.heappop(q)
            
            ma=max(ma,s*l[i][1])
        return ma%((10**9)+7)

            
            
            

