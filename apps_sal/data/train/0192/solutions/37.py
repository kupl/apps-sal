class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        print(piles)
        sumval = 0
        for i in range(1,len(piles)*2//3,2):
            sumval += piles[i]
        
        return sumval
