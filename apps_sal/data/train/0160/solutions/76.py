class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        self.memo = {}
        
        def dfs(l, r, isAlex, alexSum, leeSum):
            key = (l, r, isAlex)
            
            if key in self.memo:
                return self.memo[key]
            
            if l == r:
                leeSum += piles[l]
                r = (alexSum > leeSum)
                self.memo[key] = r
                return r
            
            if isAlex:
                r1 = dfs(l+1, r, False, alexSum + piles[l], leeSum)
                r2 = dfs(l, r-1, False, alexSum + piles[r], leeSum)
            else:
                r1 = dfs(l+1, r, True, alexSum, leeSum + piles[l])
                r2 = dfs(l, r-1, True, alexSum, leeSum + piles[r])
                
            self.memo[key] = r1 or r2
            return r1 or r2
        
        return dfs(0, len(piles) -1, True, 0, 0)
