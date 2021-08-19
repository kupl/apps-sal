class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        length = len(piles) // 3
        piles = piles[length:]
        me = 0
        alice = 0
        for i in range(len(piles)):
            if i % 2 == 0:
                me += piles[i]
            else:
                alice += piles[i]
        return me
