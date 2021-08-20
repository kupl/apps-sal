class Solution:

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        @lru_cache(None)
        def fuck(start, last, c, left):
            if start >= len(s):
                return 0
            if left == 0:
                return (1 if c == 99 or c == 9 or c == 1 else 0) + fuck(start + 1, last, c + 1, left) if s[start] == last else 1 + fuck(start + 1, s[start], 1, left)
            return (1 if c == 99 or c == 9 or c == 1 else 0) + fuck(start + 1, last, c + 1, left) if s[start] == last else min(fuck(start + 1, last, c, left - 1), 1 + fuck(start + 1, s[start], 1, left))
        return fuck(0, 'sb', 0, k)
