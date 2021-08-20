class Solution:

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations)
        h = 0
        for (index, c) in enumerate(citations):
            if c <= len(citations) - index:
                if c > h:
                    h = c
            else:
                if len(citations) - index > h:
                    h = len(citations) - index
                break
        return h
