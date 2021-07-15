class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return self.getmax(piles, 0, 0, len(piles)-1, {}) > 0
    
    def getmax(self, piles, p, i, j, cache):
        if (i > j):
            return 0
        if (i,j,p) in cache:
            return cache[(i,j,p)]
        if p == 0:
            cache[(i,j,p)] = max(piles[i] + self.getmax(piles, 1, i+1, j, cache), piles[j] + self.getmax(piles, 1, i, j-1, cache))
        else:
            cache[(i,j,p)] = min(-piles[i] + self.getmax(piles, 0, i+1, j, cache), -piles[j] + self.getmax(piles, 0, i, j-1, cache))
        return cache[(i,j,p)]
