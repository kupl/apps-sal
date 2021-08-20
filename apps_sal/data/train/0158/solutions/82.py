from functools import lru_cache


class Solution:

    def kSimilarity(self, A: str, B: str) -> int:

        @lru_cache(None)
        def solve(s1, s2):
            if not s1:
                return 0
            if s1[0] == s2[0]:
                return solve(s1[1:], s2[1:])
            ans = 21
            for (i, c) in enumerate(s1):
                if s2[0] == c:
                    ans = min(ans, 1 + solve(s1[1:i] + s1[0] + s1[i + 1:], s2[1:]))
            return ans
        return solve(A, B)
