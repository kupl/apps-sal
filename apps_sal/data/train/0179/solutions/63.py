class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        @lru_cache(None)
        def dp(index, last_char, running_length, k):
            if index >= len(s):
                return 0
            if k < 0:
                return 9999999
            if s[index] == last_char:
                extra = 0
                if running_length == 1 or running_length == 9 or running_length == 99:
                    extra += 1
                incl = extra + dp(index + 1, s[index], running_length + 1, k)
                excl = 99999
                if k > 0:
                    excl = dp(index + 1, last_char, running_length, k - 1)
                return min(incl, excl)
            incl = 1 + dp(index + 1, s[index], 1, k)
            excl = 99999
            if k > 0:
                excl = dp(index + 1, last_char, running_length, k - 1)
            return min(incl, excl)
        return dp(0, '', 0, k)
