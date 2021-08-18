class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        me = 0
        piles = sorted(piles)
        while(len(piles) > 1):
            temp = [piles[0]] + piles[-2:]
            piles.pop(0)
            piles.pop(-1)
            piles.pop(-1)
            temp = sorted(temp)
            me += temp[1]
        return me
