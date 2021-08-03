class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ret = 0
        LEN = len(piles)
        for i in range(LEN // 3):
            # print(i, LEN-(i*2+1),  piles[LEN-(i*2+1)] )
            ret += piles[LEN - (i * 2 + 2)]
        return ret
