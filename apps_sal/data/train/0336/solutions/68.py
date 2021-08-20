class Solution:

    def minSteps(self, s: str, t: str) -> int:
        s_count = {}
        t_count = {}
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]
            if s_char in s_count:
                s_count[s_char] += 1
            else:
                s_count[s_char] = 1
            if t_char in t_count:
                t_count[t_char] += 1
            else:
                t_count[t_char] = 1
        for c in t_count:
            if c in s_count:
                s_count[c] = abs(s_count[c] - t_count[c])
            else:
                s_count[c] = t_count[c]
        return sum(s_count.values()) // 2
