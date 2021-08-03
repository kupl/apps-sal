class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        ''' Use Math one-liner: return True
        Solution 1. Dynamic Programming:'''
        n = len(piles)

        @lru_cache(None)
        def dp(i, j):
            if i > j:
                return 0
            parity = (j - i - n) % 2
            if parity == 1:  # first player
                return max(piles[i] + dp(i + 1, j), piles[j] + dp(i, j - 1))
            else:
                return min(-piles[i] + dp(i + 1, j), -piles[j] + dp(i, j - 1))
        return dp(0, n - 1) > 0
