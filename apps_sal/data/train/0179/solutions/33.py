class Solution:

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        dp_cache = dict()

        def dp(i, k):
            if k < 0:
                return n
            if i + k >= n:
                return 0
            if (i, k) in dp_cache:
                return dp_cache[i, k]
            ans = dp(i + 1, k - 1)
            l = 0
            same = 0
            for j in range(i, n):
                if s[j] == s[i]:
                    same += 1
                    if same <= 2 or same == 10 or same == 100:
                        l += 1
                diff = j - i + 1 - same
                if diff < 0:
                    break
                ans = min(ans, l + dp(j + 1, k - diff))
            dp_cache[i, k] = ans
            return ans
        return dp(0, k)
