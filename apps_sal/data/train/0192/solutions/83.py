class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        p = sorted(piles)
        n = len(piles)
        
        
        res = 0
        
        l, r = 0, n - 1
        
        while l < r:
            res += p[r - 1]
            l += 1
            r -= 2
        
        return res
