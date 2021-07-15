class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        #if s[i] != s[i-1]: dp[i][t] = min(dp[i-1][t-1], dp[i-1][t] + 1)
        #else: dp[i][t] = min(dp[i-1][t-1], dp[i-1][t] + carry) carry = (cnt in [9, 99, 999]) cnt += 1
        n = len(s)
        cp = s[:]
        @lru_cache(None)
        def dp(i, last, curlen, k):
            if k < 0: return n+1
            if i >= n:
                return 0
            res = n+1
            if s[i] == last:
                carry = (curlen in [1, 9, 99])
                res = carry + dp(i+1, last, curlen+1, k)
            else:
                res = min(1+ dp(i+1, s[i], 1, k),
                         dp(i+1, last, curlen, k-1))
            return res
        
        return dp(0, '.', 0, k)
            

