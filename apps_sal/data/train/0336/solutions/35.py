class Solution:

    def minSteps(self, s: str, t: str) -> int:
        for i in range(0, len(t)):
            if t[i] in s:
                s = s.replace(t[i], '', 1)
        return len(s)
