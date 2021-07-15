class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        if len(piles) < 3:
            return 0
        res = 0
        piles.sort()
        for i in range(1,len(piles)//3+1):
            res = res + piles[(len(piles)) - (i*2)]  #((i*3)-i)]
            
        return res

