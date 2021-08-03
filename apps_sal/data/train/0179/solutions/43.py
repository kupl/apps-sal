from functools import lru_cache


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        if len(s) - k <= 1:
            return len(s) - k

        @lru_cache(None)
        def run(i, j, k, l):
            if k < 0:
                return 10000

            if i == len(s):
                return 0

            c = s[i]
            if c == j:
                return run(i + 1, c, k, l + 1) + (1 if l in [1, 9, 99] else 0)

            return min(
                run(i + 1, j, k - 1, l),
                run(i + 1, c, k, 1) + 1,
            )

        return run(0, None, k, 0)
