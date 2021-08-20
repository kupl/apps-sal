class Solution:

    def minDays(self, n: int) -> int:

        @lru_cache(None)
        def solve(n):
            if n <= 1:
                return n
            return 1 + min(n % 2 + solve(n // 2), n % 3 + solve(n // 3))
        return solve(n)
