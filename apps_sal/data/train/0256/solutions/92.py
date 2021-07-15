class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        
        def is_feasible(rate,H,piles):
            
            count=0
            for i in range(len(piles)):
                count+=piles[i]//rate
                
                if piles[i]%rate!=0:
                    count+=1
                
                if count>H:
                    return False
            
            return True
    
    
        
        l=1
        h=sum(piles)
        ans=float('inf')
        
        while l<=h:
            mid=(l+h)//2
            
            if is_feasible(mid,H,piles):
                ans=min(ans,mid) 
                h=mid-1
            
            else:
                l=mid+1
        
        return ans
            
            
                    

