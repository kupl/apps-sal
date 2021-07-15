class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        a=len(piles)//3
        
        i=0
        k=1
        piles.sort(reverse=True)
        z=0
        
        while i<a:
            z+=piles[k]
            k=k+2
            i=i+1
        return z
            
            
            

