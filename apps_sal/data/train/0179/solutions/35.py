class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def cmp(n):
            if n <= 0:
                return 0
            if n == 1:
                return 1
            if n < 10:
                return 2
            if n >= 100:
                return 4
            return 3

        @lru_cache(None)
        def solve(l, k):
            if k < 0:
                return 10000
            if l >= len(s):
                return 0
            ans = solve(l + 1, k - 1)
            ad, de = 0, 0
            for i in range(l, len(s)):
                if s[i] == s[l]:
                    ad += 1
                else:
                    de += 1
                ans = min(ans, cmp(ad) + solve(i + 1, k - de))
            return ans

        return solve(0, k)
