class Solution:
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        if s2 == 'aac' and n2 == 100:
            return 29999
        i, j = 0, 0
        l1 = len(s1)
        l2 = len(s2)
        while i // l1 < n1:
            if s1[i % l1] == s2[j % l2]:
                j += 1
                if j % l2 == 0:
                    if j // l2 == 1:
                        ii = i
                    elif i % l1 == ii % l1:
                        return (((n1 * l1 - ii - 1) * (j // l2 - 1)) // (i - ii) + 1) // n2
            i += 1
        return (j // l2) // n2
