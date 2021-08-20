class Solution:

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        @lru_cache(None)
        def get(index, left, c, streak):
            val = (1 + len(str(streak)) - (streak == 1)) * (streak > 0)
            if left < 0 or index == len(s):
                return 1000000.0 if left < 0 else val
            return min(val * (c != s[index]) + get(index + 1, left, s[index], 1 + streak * (c == s[index])), get(index + 1, left - 1, c, streak))
        return get(0, k, None, 0)
