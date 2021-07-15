class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        count = 0
        piles.sort()
        
        while len(piles) > 0:
            
            #Alice's pick
            piles.pop(-1)
            
            #My pick
            count += piles[-1]
            piles.pop(-1)
            
            #What Bob gets
            piles.pop(0)
        
        return count
