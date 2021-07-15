class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        ans = 0
        i = 1
        j = len(piles)-1
        
        while(j-i >= 1):
            ans+=piles[i]
            j-=1
            i+=2
        return ans

