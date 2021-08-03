class Solution:
    """
    time: O(logn)
    """

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0

        n = len(citations)
        left, right = 0, n - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if citations[mid] >= n - mid:
                right = mid
            else:
                left = mid

        for mid in (left, right):
            if citations[mid] >= n - mid:
                return n - mid

        return 0
