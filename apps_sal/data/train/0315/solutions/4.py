class Solution:

    def minimumSwap(self, s1: str, s2: str) -> int:
        xx = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                xx.append(s1[i])
        if len(xx) % 2 == 1:
            return -1
        res = len(xx) // 2
        if xx.count('x') % 2 == 1:
            res += 1
        return res
