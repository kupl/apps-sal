class Solution:

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        maxnum = 0
        for i in range(len(citations)):
            currH = min(citations[i], len(citations) - i)
            if currH > maxnum:
                maxnum = currH
        return maxnum
