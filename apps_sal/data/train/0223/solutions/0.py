class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        l = 0
        r = n - 1
        while l <= r:
            m = (l + r) // 2
            if m == 0 and citations[m] >= n - m or citations[m - 1] < n - (m - 1) and citations[m] >= n - m:
                return n - m
            if citations[m] < n - m:
                l = m + 1
            else:
                r = m
        return 0
