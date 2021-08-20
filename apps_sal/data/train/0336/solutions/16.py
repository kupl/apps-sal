class Solution:

    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter
        dic1 = Counter(s)
        dic2 = Counter(t)
        k = 0
        length = s.__len__()
        while k < length:
            c = t[k]
            if dic1[c] > 0:
                dic1[c] -= 1
                dic2[c] -= 1
            k += 1
        return sum(dic2.values())
