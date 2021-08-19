class Solution:

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) < len(s1):
            return False
        c1 = [0] * 128
        n = 0
        for i in s1:
            c = ord(i)
            if c1[c] == 0:
                n += 1
            c1[c] += 1
        for i in range(len(s1)):
            c = ord(s2[i])
            c1[c] -= 1
            if not c1[c]:
                n -= 1
        if not n:
            return True
        for i in range(len(s2) - len(s1)):
            c = ord(s2[i])
            if not c1[c]:
                n += 1
            c1[c] += 1
            c = ord(s2[i + len(s1)])
            c1[c] -= 1
            if not c1[c]:
                n -= 1
                if not n:
                    return True
        return False
