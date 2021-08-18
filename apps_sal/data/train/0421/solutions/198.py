class Solution:
    def lastSubstring(self, s: str) -> str:

        index = {c: i for i, c in enumerate(sorted(set(s)))}
        radix, val, cur, lo = len(index), 0, 0, 0
        for i in range(len(s) - 1, -1, -1):
            cur = index[s[i]] + cur / radix
            if cur >= val:
                lo, val = i, cur
        return s[lo:]
