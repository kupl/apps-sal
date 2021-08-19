class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        s = 0
        for i in range(0, len(piles), 2):
            x = piles.pop()
            try:
                s += piles[i + 1]
            except:
                print('')
        return s
