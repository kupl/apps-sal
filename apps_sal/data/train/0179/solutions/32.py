class Solution:

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)

        @lru_cache(None)
        def dp(i, k):
            if k < 0:
                return n
            if i + k >= n:
                return 0
            res = dp(i + 1, k - 1)
            l = 0
            same = 0
            for j in range(i, n):
                if s[j] == s[i]:
                    same += 1
                    if same <= 2 or same == 10 or same == 100:
                        l += 1
                diff = j - i + 1 - same
                res = min(res, l + dp(j + 1, k - diff))
            return res
        return dp(0, k)
