from functools import lru_cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)
        
        @lru_cache(None)
        def dp(i,j):
            if i > j:
                return 0
            parity = (N - (j-i+1)) % 2 #0-alex, 1-lee
            # parity = (j-i-N) % 2
            if parity == 0 :
                return max(piles[i] + dp(i+1,j), piles[j]+dp(i,j-1))
            else:
                return min(-piles[i] + dp(i+1,j), -piles[j] + dp(i,j-1))
            
        return dp(0, N-1) > 0
