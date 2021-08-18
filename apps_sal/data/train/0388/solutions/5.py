class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations) == 0:
            return 0

        maxCita = -sys.maxsize - 1
        for citation in citations:
            maxCita = max(maxCita, citation)

        start = 0
        end = len(citations)

        while start <= end:
            mid = start + (end - start) // 2
            if self.countGreater(mid, citations) > mid:
                start = mid + 1
            else:
                end = mid - 1

        if self.countGreater(end, citations) <= end:
            return end
        else:
            return start

    def countGreater(self, cita, citations):
        count = 0
        for citation in citations:
            if citation > cita:
                count += 1
        return count
