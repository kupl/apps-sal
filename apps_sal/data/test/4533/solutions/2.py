class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i, j = 0, 0
        happyKids = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                happyKids += 1
                i += 1
            j += 1
        return happyKids
