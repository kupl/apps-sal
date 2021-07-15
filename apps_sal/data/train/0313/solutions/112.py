class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def feasible(limit):
            flower=bouquets=0
            for day in bloomDay:
                if day<=limit:
                    bouquets+=(flower+1)//k
                    flower=(flower+1)%k
                else:
                    flower=0
                    
            return bouquets>=m
        
        
        if len(bloomDay)<m*k:return -1
    
        left,right=1,max(bloomDay)
        
        while left<right:
            
            mid=(left+right)//2
            
            if feasible(mid):
                right=mid
            
            else:
                left=mid+1
                
        return left
    
        
                    
                    
                    
                    
                    
                    
                
                
    
        

