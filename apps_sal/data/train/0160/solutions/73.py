class Solution:
    def stoneGame(self, piles):
        cache = {}
        piles = tuple(piles)
        
    
        res = [0]
        for k in range(len(piles)):
            res.append(res[-1] + piles[k])
        
        
        def firstscore(i,j):
            if i>=j: return 0
            if j==i+1 and j < len(piles): return piles[i]
            if (i,j) in cache: return cache[i,j]
            r = max(res[j] - res[i] - firstscore(i + 1, j), res[j] - res[i] - firstscore(i, j - 1))
            cache[i,j] = r
            return r

        Alex = firstscore(0,len(piles))
        Lee = sum(piles) - Alex
        return Alex > Lee
