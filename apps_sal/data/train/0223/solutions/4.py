class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h = 0
        count = 0
        for c in citations[::-1]:
            if c <= count:
                return count
            count += 1
        return count
