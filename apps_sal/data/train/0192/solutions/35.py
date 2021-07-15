class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        # print(piles)
        res = 0
        tims = len(piles)//3
        for i in range(1,len(piles)-tims,2):
            res += piles[i]
        return res 
        pass
