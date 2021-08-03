class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def count(start, pre, pre_count, k):
            if k < 0:
                return float('inf')
            if len(s) - start <= k:
                return 0

            if s[start] == pre:
                incr = 1 if pre_count == 1 or pre_count == 9 or pre_count == 99 else 0
                return incr + count(start + 1, pre, pre_count + 1, k)
            else:
                delete = count(start + 1, pre, pre_count, k - 1)
                keep = 1 + count(start + 1, s[start], 1, k)
                return min(delete, keep)

        return count(0, '', 0, k)
