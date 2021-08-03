class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        c = citations
        if not c:
            return 0
        s, e = 0, len(c) - 1
        if c[s] >= len(c):
            return len(c)
        if c[e] < 1:
            return 0
        while s < e - 1:
            m = s + int((e - s) / 2)
            if c[m] >= len(c) - m:
                e = m
            else:
                s = m
        return len(c) - e
