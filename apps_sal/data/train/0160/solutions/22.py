class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        @lru_cache(None)
        def helper(start=0, end=len(piles)):
            if end - start == 2:
                return (max(piles), min(piles))

            leeL, alexL = helper(start + 1, end)
            alexL += piles[start]

            leeR, alexR = helper(start, end - 1)
            alexR += piles[end - 1]

            return (alexR, leeR) if alexR > alexL else (alexL, leeL)

        alex, lee = helper()
        return alex > lee
