class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles=sorted(piles)
        sum=0
        for n in range(len(piles)//3,len(piles),2):
            sum=sum+piles[n]
        return(sum)
