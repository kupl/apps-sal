class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        return sum(piles[int(len(piles) / 3):-1:2])
        '\n        # We want to pick two large numbers and one small number\n        our_coins = 0\n        our_piles = 0\n        l = len(piles)//3\n        piles.sort()\n        pointer = -2\n        while our_piles < l:\n            our_piles+=1\n            our_coins+=piles[pointer]\n            pointer-=2\n        return our_coins\n        '
