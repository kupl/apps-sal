class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        if not piles: return -1
        
        low,high=1,sum(piles)
        
        def isPossible(piles,target,H):
            
            return sum(math.ceil(p/target) for p in piles) <= H
       
        while low < high:
            
            mid = low+(high-low)//2
            # print(low,high,mid)
            if isPossible(piles,mid,H):
                high = mid
            else:
                low = mid+1
                
        return low
        

