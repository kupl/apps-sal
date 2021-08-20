class Solution:

    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        (index, result) = (0, 0)
        while index < len(s) and len(g) > 0:
            if s[index] >= g[0]:
                result += 1
                index += 1
                g.remove(g[0])
            else:
                index += 1
        return result
