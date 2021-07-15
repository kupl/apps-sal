class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        alex = 0
        lee = 0
        
        alex_turn = True
        
        while len(piles) != 0:
            maxi = (-1,0)
            for i in range(len(piles)):
                if piles[i] > maxi[0]:
                    maxi = (piles[i], i)

            piles.pop(maxi[1])
            if alex_turn:
                alex += maxi[0]
                alex_turn = False
            else:
                lee += maxi[0]
                alex_turn = True
        
        if alex > lee:
            return True
        return False
