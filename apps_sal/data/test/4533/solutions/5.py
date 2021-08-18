class Solution:

    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        s.sort()
        g.sort()
        total = 1
        child_to_give = []
        child_index = 0

        start_i = 0
        for j in range(0, len(g)):
            for i in range(start_i, len(s)):
                if s[i] >= g[j]:
                    child_to_give.append(j)
                    start_i = i + 1
                    break

        print(child_to_give)
        return len(child_to_give)
