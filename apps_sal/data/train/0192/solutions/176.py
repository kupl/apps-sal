class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n=len(piles)//3
        piles.sort()
        count=0
        i=n
        while i < len(piles):
            count+=piles[i]
            i+=2
        return(count)

