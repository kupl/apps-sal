class Solution:

    def minSteps(self, s: str, t: str) -> int:
        ms = {}
        for c in s:
            old = ms.get(c, 0)
            ms[c] = old + 1
        count = 0
        for c in t:
            old = ms.get(c, 0)
            if old == 0:
                count += 1
            else:
                ms[c] -= 1
        return count
