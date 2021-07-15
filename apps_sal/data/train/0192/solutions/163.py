class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort(reverse = True)
        print(piles)
        p3n = len(piles)
        n = int(p3n/3)
        out = 0
    
        i = 1
        while i < 2*n:
            out += piles[i]
            print((piles[i]))
            i += 2
        
        return out
        

