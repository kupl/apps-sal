class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0

        sorted_ci = list(sorted(citations))
        i = 0
        while i < len(sorted_ci) and sorted_ci[len(citations) - i - 1] >= i + 1:
            i += 1
        return i
