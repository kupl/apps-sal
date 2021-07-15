class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        count=0
        i=len(piles)-2
        res=0
        take=len(piles)//3
        while count != take: 
            res+=piles[i]
            i-=2
            count+=1
        return(res)
