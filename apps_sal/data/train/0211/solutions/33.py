class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)

        @lru_cache(None)
        def dp(i, cur):
            nonlocal ans
            if len(cur) + n - i < ans:
                return
            if i >= n:
                ans = max(ans, len(cur))
            l = n - i
            for k in range(1, l + 1):
                cand = s[i:i + k]
                if cand not in cur:
                    dp(i + k, cur + (cand,))
        ans, cur = 0, ()
        dp(0, cur)
        return ans
