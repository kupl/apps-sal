class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        maxI, center, right = 0, 0, 0
        stL = self.addChar(s)
        pal = [0] * len(stL)
        for i in range(1, len(stL) - 1):
            currI = 2 * center - i
            if right > i:
                pal[i] = min(right - i, pal[currI])
            else:
                pal[i] = 0
            while stL[i + 1 + pal[i]] == stL[i - 1 - pal[i]]:
                pal[i] += 1
            if i + pal[i] > right:
                center, right = i, i + pal[i]
        for i in range(1, len(stL) - 1):
            if pal[i] > pal[maxI]:
                maxI = i
        start = (maxI - 1 - pal[maxI]) // 2
        return s[start:start + pal[maxI]]

    def addChar(self, st):
        stLs = ['<']
        for c in st:
            stLs.extend(['#', c])
        stLs.extend(['#', '>'])
        return stLs
