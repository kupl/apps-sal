class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        c1 = collections.Counter(s1)
        c2 = collections.Counter(s2)
        t1,t2 = 0,0
        f1,f2 = 1,1
        for i in range(26):
            z = chr(97+i)
            t1 += c1[z] - c2[z]
            if t1 < 0:
                f1 = 0
            t2 += c2[z] - c1[z]
            if t2 < 0:
                f2 = 0
        return f1 or f2
