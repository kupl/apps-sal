class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        if len(piles) == 2:
            return True

        alex = 0
        lee = 0

        i = 0

        while(i < len(piles)):

            if i % 2 == 0:
                alex += max(piles[0], piles[len(piles) - 1])
                piles.remove(max(piles[0], piles[len(piles) - 1]))

            else:
                lee += min(piles[0], piles[len(piles) - 1])
                piles.remove(min(piles[0], piles(len(piles) - 1)))

        if alex > lee:
            return True
        return False
