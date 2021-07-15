class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = 0
        for i in s:
            if i in t:
                t = t.replace(i, '', 1)
            else:
                count += 1
        return count
