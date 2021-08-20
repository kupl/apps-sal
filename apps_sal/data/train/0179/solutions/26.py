class Solution:

    def getLengthOfOptimalCompression(self, s, k):
        memo = {}

        def counter(start, last_char, last_char_len, rem_chars):
            nonlocal memo, s
            if rem_chars < 0:
                return float('inf')
            if start == len(s):
                return 0
            if (start, last_char, last_char_len, rem_chars) not in memo:
                if s[start] == last_char:
                    inc = 1 if last_char_len in (1, 9, 99) else 0
                    memo[start, last_char, last_char_len, rem_chars] = inc + counter(start + 1, last_char, last_char_len + 1, rem_chars)
                else:
                    keep_len = 1 + counter(start + 1, s[start], 1, rem_chars)
                    rem_len = counter(start + 1, last_char, last_char_len, rem_chars - 1)
                    memo[start, last_char, last_char_len, rem_chars] = min(keep_len, rem_len)
            return memo[start, last_char, last_char_len, rem_chars]
        return counter(0, '', 0, k)
