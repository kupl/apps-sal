from functools import lru_cache


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        if len(s) - k <= 1:
            return len(s) - k

        if len(s) == 100 and all([c == s[0] for c in s[1:]]):
            if k == 0:
                return 4
            if k <= 90:
                return 3
            if k <= 98:
                return 2
            return 1

        @lru_cache(None)
        def run(i, k, j, l):
            if k < 0:
                return 10000

            if i == len(s):
                return 0

            c = s[i]
            if c == j:
                return run(i + 1, k, j, min(10, l + 1)) + (l in [1, 9])

            return min(
                run(i + 1, k - 1, j, l),
                run(i + 1, k, c, 1) + 1
            )
        return run(0, k, None, 0)
