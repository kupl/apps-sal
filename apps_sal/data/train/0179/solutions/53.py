class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        N = len(s)
        
        @lru_cache(None)
        def rec(cur, rem, ln, ch):
            if rem < 0:
                return math.inf
            if cur == N:
                return 0
            
            ans = math.inf
            if s[cur] == ch:
                add = (ln == 1 or ln == 9 or ln == 99)
                ans = rec(cur+1, rem, ln + 1, ch) + add
            else:
                ans = rec(cur+1, rem-1, ln, ch)
                ans = min(ans, rec(cur+1, rem, 1, s[cur]) + 1)
            
            return ans
        
        return rec(0, k, 0, '')

