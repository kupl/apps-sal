class Solution:

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        @lru_cache(None)
        def get(index, left, c, streak):
            if left < 0:
                return 1000000.0
            if index == len(s):
                return (1 + len(str(streak)) - (streak == 1)) * (streak > 0)
            return min((1 + len(str(streak)) - (streak == 1)) * (streak > 0) * (c != s[index]) + get(index + 1, left, s[index], 1 + streak * (c == s[index])), get(index + 1, left - 1, c, streak))
        return get(0, k, None, 0)
