class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        def inner(i,j, chance):
            if i == j and chance:
                return piles[i]
            if i > j:
                return 0
            if dp.get((i,j,chance)) == None:
                if chance:
                    dp[(i,j,chance)] = max(piles[i]+inner(i+1,j, False), piles[j]+inner(i,j-1, False))
                else:
                    dp[(i,j,chance)] = max(inner(i+1,j, True), inner(i,j-1, True))
            return dp[(i,j,chance)]
        a = inner(0,len(piles)-1, True)
        return True if a > (sum(piles)-a) else False

