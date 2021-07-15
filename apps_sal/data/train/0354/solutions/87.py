from functools import lru_cache

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        
        @lru_cache(None)
        def dfs(rolls_left, prev_roll, num_repeats):
            if rolls_left == 0:
                return 1
            ans = 0
            for roll in range(6):
                if roll == prev_roll:
                    if rollMax[roll] - num_repeats > 0:
                        ans += dfs(rolls_left-1, prev_roll, num_repeats+1)
                else:
                    ans += dfs(rolls_left-1, roll, 1)
            return ans % (10**9 + 7)
        
        return dfs(n, -1, 0)
