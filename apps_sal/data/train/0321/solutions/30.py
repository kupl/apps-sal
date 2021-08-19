class Solution:

    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        x = 'abcdefghijklmnopqrstuvwxyz'
        d = defaultdict(int)
        for i in range(len(x)):
            d[x[i]] = i + 1
        a1 = []
        a2 = []
        for i in range(len(s1)):
            a1.append(d[s1[i]])
            a2.append(d[s2[i]])
        a1.sort()
        a2.sort()
        (c1, c2) = (0, 0)
        for i in range(len(a1)):
            if a1[i] > a2[i]:
                c1 += 1
            elif a2[i] > a1[i]:
                c2 += 1
            else:
                c1 += 1
                c2 += 1
        if c1 == len(s1) or c2 == len(s1):
            return True
        return False
