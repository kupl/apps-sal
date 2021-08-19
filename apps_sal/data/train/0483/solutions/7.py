class Solution:

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        h = height
        most = 0
        i = 0
        j = len(h) - 1
        while i < j:
            most = max(most, (j - i) * min(h[i], h[j]))
            if h[i] < h[j]:
                i += 1
            else:
                j -= 1
        return most
