class Solution:
    def lengthLongestPath(self, inp):
        """
        :type input: str
        :rtype: int
        """
        m, l = 0, {-1: -1}
        for s in inp.split('\n'):
            d = s.count('\t')
            l[d] = 1 + l[d - 1] + len(s) - d
            if '.' in s:
                m = max(m, l[d])
        return m
