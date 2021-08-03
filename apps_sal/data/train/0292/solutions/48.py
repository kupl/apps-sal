class Solution:
    def maxAbsValExpr(self, a1: List[int], a2: List[int]) -> int:
        s1 = []
        s2 = []
        d1 = []
        d2 = []
        for i in range(len(a1)):
            s1.append(a1[i] + a2[i] + i)
            s2.append(a1[i] + a2[i] - i)
            d1.append(a1[i] - a2[i] + i)
            d2.append(a1[i] - a2[i] - i)
        return max(max(s1) - min(s1), max(s2) - min(s2), max(d1) - min(d1), max(d2) - min(d2))
