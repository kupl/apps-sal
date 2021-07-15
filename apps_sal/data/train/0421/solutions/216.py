class Solution:
    def lastSubstring(self, s: str) -> str:
        index = {c: i for i, c in enumerate(sorted(set(s)))}
        cur, radix, max_val, max_i = 0, len(index), 0, 0
        for i in range(len(s)-1, -1, -1):
            cur = index[s[i]] + cur/radix
            if cur > max_val:
                max_val, max_i = cur, i
        return s[max_i:]
