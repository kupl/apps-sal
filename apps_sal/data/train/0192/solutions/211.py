class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ans=0
        piles.sort()
        i=len(piles)-2
        j=0
        while(i>=j):
            ans=ans+piles[i]
            i=i-2
            j=j+1
        return ans
        # 1 2 3 4 5 6 7 8 9
        # 9 8 1
        # 7 6 2
        # 5 4 3

