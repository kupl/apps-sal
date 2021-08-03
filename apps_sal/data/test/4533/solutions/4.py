class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        result = 0
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                result = result + 1
                i = i + 1
                j = j + 1
            else:
                j = j + 1
        return result
