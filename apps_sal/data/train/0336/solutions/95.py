class Solution:

    def minSteps(self, s: str, t: str) -> int:
        if len(s) != len(t):
            return -1
        elif sorted(s) == sorted(t):
            return 0
        I = set(s).intersection(t)
        freq_s = {}
        for c in s:
            if c in I:
                freq_s[c] = freq_s.get(c, 0) + 1
        freq_t = {}
        for c in t:
            if c in I:
                freq_t[c] = freq_t.get(c, 0) + 1
        I_sum = 0
        for c in list(freq_t.keys()):
            freq_t[c] = min(freq_s[c], freq_t[c])
            I_sum += freq_t[c]
        return len(t) - I_sum
