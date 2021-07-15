class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        result = 0
        piles.sort(reverse = True)
        for i in range(1, 2*len(piles)//3, 2):
            result += piles[i]
        return result
            

