class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        t = 0
        i , j = 0 , n-1
        while i < j :
            t+=piles[j - 1]
            j-=2
            i+=1
        return t
