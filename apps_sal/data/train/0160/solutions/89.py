class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)
        def dp(i, j):
            # The value of the game [piles[i], piles[i+1], ..., piles[j]].
            if i > j: return 0
            parity = (j - i - N) % 2
            if parity == 1:  # first player
                return max(piles[i] + dp(i+1,j), piles[j] + dp(i,j-1))
            else:
                return min(-piles[i] + dp(i+1,j), -piles[j] + dp(i,j-1))
        
        # this is actually min max tree traversal :D
        @lru_cache(None)
        def recursion(i, j):
            if i > j:
                return 0
            curr_len = (j - i)
            if curr_len % 2 == 0:
                return min(-piles[i] + recursion(i+1, j), -piles[j] + recursion(i, j-1))
            else:
                return max(piles[i] + recursion(i+1, j), piles[j] + recursion(i, j-1))
        
        return recursion(0, N - 1) > 0
