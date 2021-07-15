class Solution:
    def minDays(self, bloom: List[int], m: int, k: int) -> int:
        def isFeasible(day):
            flower,bouqets=0,0
            for b in bloom:
                if b>day:
                    flower=0
                else:
                    bouqets+=(flower+1)//k
                    flower=(flower+1)%k
            return bouqets>=m
        
        if len(bloom) < m * k:
            return -1
        l,r=1,max(bloom)
        while l<r:
            mid=l+(r-l)//2
            if isFeasible(mid):
                r=mid
            else:
                l=mid+1
                
        return l
            
            
            

