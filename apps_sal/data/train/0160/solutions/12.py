class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)
        
        # i refers to left pointer, j refers to right pointer to piles array
        @lru_cache(None)
        def dp(i, j):
            if i > j:
                return 0
            
            parity = (j - i) % 2
            if parity == 1:
                return max(piles[i] + dp(i+1, j), piles[j] + dp(i, j-1))
            else:
                return min(-piles[i] + dp(i+1, j), -piles[j] + dp(i,j-1))
        
        return dp(0, N-1) > 0

