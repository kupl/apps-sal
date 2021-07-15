class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n=len(piles)//3
        piles.sort(reverse=True)
        count=0
        j=1
        for i in range(n):
            count+=piles[j]
            j+=2
        return count
