class Solution:

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        @lru_cache(None)
        def counter(start, last, last_cnt, left):
            if left < 0:
                return float('inf')
            if start >= len(s):
                return 0
            if s[start] == last:
                inc = 1 if last_cnt == 1 or last_cnt == 9 or last_cnt == 99 else 0
                return inc + counter(start + 1, last, last_cnt + 1, left)
            else:
                keep_c = 1 + counter(start + 1, s[start], 1, left)
                del_c = counter(start + 1, last, last_cnt, left - 1)
                return min(keep_c, del_c)
        return counter(0, '', 0, k)
