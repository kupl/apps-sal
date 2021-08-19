from collections import Counter


class Solution:

    def minSteps(self, s: str, t: str) -> int:
        d = Counter(s)
        res = 0
        for char in t:
            if d[char] > 0:
                d[char] -= 1
            else:
                res += 1
        return res
