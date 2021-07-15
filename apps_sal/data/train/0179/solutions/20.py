class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def get_length(beg: int, last_char: str, n_repeat: str, quota: int) -> int:
            if quota < 0:
                return float('inf')
            if beg == len(s):
                return 0
            if s[beg] == last_char:
                incr = 1 if n_repeat in [1, 9, 99] else 0
                return incr + get_length(beg+1, last_char, n_repeat+1, quota)
            else:
                return min(
                    get_length(beg+1, last_char, n_repeat, quota - 1), # delete this char
                    1 + get_length(beg+1, s[beg], 1, quota)
                )
        return get_length(0, '', 0, k)
