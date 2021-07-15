from functools import lru_cache
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def min_run_len(last_char, last_count, curr_idx, rest_k):
            if curr_idx == len(s):
                return 0
            
            # Keep current char
            curr_count = last_count + 1 if s[curr_idx] == last_char else 1
            incr = 1 if curr_count in [1, 2, 10, 100] else 0
            res1 = incr + min_run_len(s[curr_idx], curr_count, curr_idx + 1, rest_k)
            
            # Delete current char
            res2 = float('inf')
            if rest_k > 0:
                res2 = min_run_len(last_char, last_count, curr_idx + 1, rest_k - 1)
                
            return min(res1, res2)
        
        return min_run_len('#', 0, 0, k)

