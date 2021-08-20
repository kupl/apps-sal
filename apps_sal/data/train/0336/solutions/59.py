class Solution:

    def minSteps(self, s: str, t: str) -> int:
        s_set = set(s)
        steps = 0
        for char in s_set:
            s_charfreq = s.count(char)
            t_charfreq = t.count(char)
            if s_charfreq > t_charfreq:
                steps += s_charfreq - t_charfreq
        return steps
