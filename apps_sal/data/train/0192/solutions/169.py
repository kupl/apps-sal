class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort()
        ans = 0
        while len(piles) >=3:
            bade_bahi = piles.pop()
            mei_khud = piles.pop()
            chutiya = piles.pop(0)
            ans += mei_khud
            #piles = piles[1:-2]
        return ans
