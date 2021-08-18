class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        l = len(citations)
        if l == 0:
            return 0
        if l == 1:
            if citations[0] == 0:
                return 0
            else:
                return 1
        if min(citations) >= l:
            return l

        citations = citations[::-1]
        count = 0
        thres = 0
        i = 0
        while i < len(citations):
            if thres >= count:
                thres = citations[i]
                count += 1
                i += 1
            else:
                return count - 1
        return count - 1
