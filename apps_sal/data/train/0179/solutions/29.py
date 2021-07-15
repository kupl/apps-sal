class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)

        @lru_cache(None)
        def dp(i, k, last, last_count):
            if (n - i) <= k:
                return 0 # remove all
            
            if s[i] == last:
                inc = 1 if last_count in [1,9,99] else 0
                return inc + dp(i + 1, k, last, last_count + 1)
            else:
                res = 1 + dp(i + 1, k, s[i], 1)
                if k:
                    res = min(res, dp(i + 1, k - 1, last, last_count))
                return res

        return dp(0, k, '', 0)

