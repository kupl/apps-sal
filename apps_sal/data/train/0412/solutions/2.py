class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        @lru_cache(None)
        def solve(s, t):
            if s == 0:
                if t == 0:
                    return 1
                return 0
            ans = 0
            for i in range(1, f + 1):
                if t >= i:
                    ans += solve(s - 1, t - i)
            return ans
        return solve(d, target) % (10**9 + 7)
