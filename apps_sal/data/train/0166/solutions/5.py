class Solution:

    def minFlips(self, a: int, b: int, c: int) -> int:
        stra = '{0:b}'.format(a)
        strb = '{0:b}'.format(b)
        strc = '{0:b}'.format(c)
        n = max(len(stra), len(strb), len(strc))
        stra = '0' * (n - len(stra)) + stra
        strb = '0' * (n - len(strb)) + strb
        strc = '0' * (n - len(strc)) + strc
        boolA = [s == '1' for s in stra]
        boolB = [s == '1' for s in strb]
        boolC = [s == '1' for s in strc]
        x = 0
        for i in range(n):
            (A, B, C) = (boolA[i], boolB[i], boolC[i])
            if not (A or B) == C:
                if A and B:
                    x += 2
                else:
                    x += 1
        return x
