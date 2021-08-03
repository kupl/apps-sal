from functools import lru_cache


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        # dp[idx,prev]  = (dp[idx-1,prev] +
        @lru_cache(None)
        def helper(idx, prev):
            e, c = prev
            if idx == n:
                return 1
            count = 0
            for i in range(6):
                if e == i:
                    if c < rollMax[i]:
                        count += helper(idx + 1, (i, c + 1)) % (10**9 + 7)
                else:
                    count += helper(idx + 1, (i, 1)) % (10**9 + 7)
            return count % (10**9 + 7)
        return helper(0, (-1, 0)) % (10**9 + 7)
