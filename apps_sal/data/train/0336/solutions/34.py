class Solution:

    def minSteps(self, s: str, t: str) -> int:
        count = 0
        for curr in s:
            if curr in t:
                t = t.replace(curr, '', 1)
            else:
                count += 1
        return count
