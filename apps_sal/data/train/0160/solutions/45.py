class Solution:

    def stoneGame(self, piles: List[int]) -> bool:

        def pmin(i, j):
            if (i, j) in mincache:
                return mincache[i, j]
            elif i == j:
                return piles[i]
            mincache[i, j] = min(pmax(i + 1, j), pmax(i, j - 1))
            return mincache[i, j]

        def pmax(i, j):
            if (i, j) in maxcache:
                return maxcache[i, j]
            elif i == j:
                return piles[i]
            maxcache[i, j] = max(piles[i] + pmin(i + 1, j), piles[j] + pmin(i, j - 1))
            return maxcache[i, j]
        (mincache, maxcache) = ({}, {})
        p1 = pmax(0, len(piles) - 1)
        p2 = sum(piles) - p1
        return p1 > p2
