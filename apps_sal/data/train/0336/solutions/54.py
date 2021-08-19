class Solution:

    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter
        (counterS, counterT) = (Counter(s), Counter(t))
        res = 0
        for i in counterS:
            res += max(0, counterS[i] - counterT[i])
        return res
