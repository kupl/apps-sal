from functools import lru_cache

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
            
        @lru_cache(None)
        def dfs(start, last_ch, count, k):
            if k < 0:
                return float('inf')
            if start >= len(s):
                return 0
            if s[start] == last_ch:
                return dfs(start+1, last_ch, count+1, k) + ( 1 if count in {1, 9, 99, 99} else 0 )
            else:
                keep = 1 + dfs(start+1, s[start], 1, k)
                discard = dfs(start+1, last_ch, count, k - 1)
                return min(keep, discard)
        
        return dfs(0, '', 0, k)

