class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = 0
        a = s
        b = t
        if len(s) == 0:
            return len(t)
        if len(t) == 0:
            return len(s)
        for curr in a:
            if curr in b:
                b = b.replace(curr, '', 1)
            else:
                count += 1
        return count
