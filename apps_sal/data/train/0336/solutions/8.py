class Solution:
    def minSteps(self, s: str, t: str) -> int:
        minSteps = 0
        dict = {}
        for ch in s:
            if dict.get(ch):
                dict[ch] += 1
            else:
                dict[ch] = 1
        for c in t:
            num = dict.get(c)
            if num:
                dict[c] -= 1
                if num < 0:
                    minSteps += 1
            else:
                minSteps += 1

        return minSteps
