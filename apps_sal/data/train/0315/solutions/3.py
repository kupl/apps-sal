class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        cntxy, cntyx, n = 0, 0, len(s1)
        for i in range(n):
            if s1[i] == 'x' and s2[i] == 'y': cntxy += 1
            elif s1[i] == 'y' and s2[i] == 'x': cntyx += 1
        if (cntxy + cntyx) % 2 == 1: return -1
        if cntxy % 2 == 1:
            return cntxy // 2 + cntyx // 2 + 2
        else: return cntxy // 2 + cntyx // 2

