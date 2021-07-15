class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        count = 0
        for i in range(len(piles) - 2, len(piles)//3 - 1, -2):
            count += piles[i]
        
        # while piles:
        #     piles.pop()
        #     count += piles.pop()
        #     piles.pop(0)
        return count
