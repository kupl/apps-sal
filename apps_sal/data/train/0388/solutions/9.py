class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        citations.sort()
        for i in range(N):
            if citations[i] < N - i:
                continue
            else:
                return N - i
        return 0
