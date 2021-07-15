from functools import lru_cache

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def compress(now, prev_ch, prev_count, left):
            if left < 0: return len(s) + 1
            if now >= len(s): return 0
            if s[now] == prev_ch:
                incr = 1 if prev_count == 1 or prev_count == 9 or prev_count == 99 else 0
                return incr + compress(now + 1, prev_ch, prev_count + 1, left)
            keep = 1 + compress(now + 1, s[now], 1, left)
            delete = compress(now + 1, prev_ch, prev_count, left - 1)
            return min(keep, delete)
        
        return compress(0, '', 0, k)
