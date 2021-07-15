class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # the same thing, but faster and more pythonic
        piles.sort()
        return sum(piles[int(len(piles) / 3): -1 : 2])
        '''
        # We want to pick two large numbers and one small number
        our_coins = 0
        our_piles = 0
        l = len(piles)//3
        piles.sort()
        pointer = -2
        while our_piles < l:
            our_piles+=1
            our_coins+=piles[pointer]
            pointer-=2
        return our_coins
        '''
